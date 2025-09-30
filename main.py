import os
import yaml
import shutil
import markdown

# from typing import List
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader("templates"))


def parse_markdown(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        raw = file.read()
    if raw.startswith("---"):
        _, fm, content = raw.split("---", 2)
        metadata = yaml.safe_load(fm)
    else:
        metadata = {}
        content = raw

    md = markdown.Markdown(
        extensions=["fenced_code", "tables", "codehilite"],
        extension_configs={
            "pymdownx.arithmatex": {
                "generic": True,  # Output <span class="arithmatex">...</span>
                "preview": False,  # Don’t show fallback preview
            }
        },
    )
    html = md.convert(content)
    metadata["content"] = html
    metadata["slug"] = os.path.splitext(os.path.basename(file_path))[0] + ".html"
    return metadata


def render_index():
    template = env.get_template("index.html")
    metadata = parse_markdown("content/index.md")
    render = template.render(metadata=metadata)
    output_path = os.path.join("public", "index.html")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(render)


def render_books():
    template = env.get_template("curated-books.html")
    metadata = parse_markdown("content/books.md")
    render = template.render(metadata=metadata)
    output_path = os.path.join("public", "books.html")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(render)


def render_rss(posts):
    template = env.get_template("rss.xml")
    site_info = {
        "title": "Gautam Singh",
        "url": "pikachu-cell.github.io",
        "description": "Posts on math, code, and AI",
    }

    # Sort by date descending
    sorted_posts = sorted(posts, key=lambda x: x["date"], reverse=True)

    rss = template.render(site=site_info, posts=sorted_posts)

    output_path = os.path.join("public", "rss.xml")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(rss)


def render_posts(posts):
    template = env.get_template("posts.html")
    sorted_posts = sorted(posts, key=lambda x: x["date"], reverse=True)
    render = template.render(posts=sorted_posts)
    output_path = os.path.join("public", "posts.html")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(render)


def render_tag(tag):
    pass


def render_post(filename, metadata):
    template = env.get_template("post.html")
    render = template.render(metadata=metadata)
    output_path = os.path.join("public/posts", filename[:-3] + ".html")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(render)
    pass


# def get_tags() -> List[str]:
#     pass


def build():
    os.makedirs("public", exist_ok=True)
    os.makedirs("public/posts", exist_ok=True)
    shutil.copytree("static", "public/static", dirs_exist_ok=True)

    render_index()
    render_books()

    posts = []

    for filename in os.listdir("content/posts"):
        if filename.endswith(".md"):
            metadata = parse_markdown(os.path.join("content/posts", filename))
            posts.append(
                dict(
                    date=metadata["date"],
                    meta=dict(title=metadata["title"], slug=metadata["slug"]),
                )
            )
            render_post(filename, metadata=metadata)

    render_posts(posts)
    render_rss(posts)
    # tags = get_tags()

    # for tag in tags:
    #     render_tag(tag)


if __name__ == "__main__":
    build()
