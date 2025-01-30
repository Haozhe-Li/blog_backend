from flask import Flask
import markdown2
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
from flask import send_file
import json
import os

app = Flask(__name__)

blogs_folder = "blogs"


@app.route("/get")
def home():
    response = []
    for blog in os.listdir(blogs_folder):
        if blog.startswith("."):
            continue
        with open(f"{blogs_folder}/{blog}/overview.json", "r") as f:
            overview = json.load(f)
        response.append(overview)
    response.sort(key=lambda x: x["date"], reverse=True)
    return {"blogs": response}

@app.route("/get/<blog_id>/cover")
def get_cover_img(blog_id):
    with open(f"{blogs_folder}/{blog_id}/overview.json", "r") as f:
        overview = json.load(f)
    cover_img_path = f"{blogs_folder}/{blog_id}/{overview['cover']}"
    return send_file(cover_img_path, mimetype='image/jpeg')

@app.route("/get/<blog_id>")
def get_blog(blog_id):
    with open(f"{blogs_folder}/{blog_id}/content.md", "r") as f:
        blog_content = f.read()
    
    # Convert markdown to HTML with code highlighting
    blog_html = markdown2.markdown(blog_content, extras=["fenced-code-blocks", "code-friendly"])

    # Highlight code blocks
    def highlight_code(html):
        lexer = get_lexer_by_name("python", stripall=True)
        formatter = HtmlFormatter()
        return highlight(html, lexer, formatter)

    blog_html = highlight_code(blog_html)

    with open(f"{blogs_folder}/{blog_id}/overview.json", "r") as f:
        overview = json.load(f)
    overview["content"] = blog_html
    return {"blog": overview}


if __name__ == "__main__":
    app.run(debug=True)
