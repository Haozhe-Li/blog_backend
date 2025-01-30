from flask import Flask, send_file
import markdown2
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
import json
import os

# Initialize the Flask application
app = Flask(__name__)

# Define the folder where blog data is stored
blogs_folder = "blogs"

@app.route("/get")
def home():
    """
    Endpoint to get the list of all blogs.
    Reads the overview.json file from each blog folder and returns a sorted list of blogs by date.
    """
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
    """
    Endpoint to get the cover image of a specific blog.
    Reads the overview.json file to get the cover image path and returns the image file.
    """
    with open(f"{blogs_folder}/{blog_id}/overview.json", "r") as f:
        overview = json.load(f)
    cover_img_path = f"{blogs_folder}/{blog_id}/{overview['cover']}"
    return send_file(cover_img_path, mimetype="image/jpeg")

@app.route("/get/<blog_id>")
def get_blog(blog_id):
    """
    Endpoint to get the content of a specific blog.
    Reads the content.md file, converts it to HTML with syntax highlighting, and returns the blog overview with content.
    """
    # Read the markdown content of the blog
    with open(f"{blogs_folder}/{blog_id}/content.md", "r") as f:
        blog_content = f.read()

    # Convert markdown content to HTML
    blog_html = markdown2.markdown(
        blog_content, extras=["fenced-code-blocks", "code-friendly"]
    )

    # def highlight_code(html):
    #     """
    #     Function to highlight code blocks in the HTML content.
    #     Uses Pygments to apply syntax highlighting.
    #     """
    #     lexer = get_lexer_by_name("python", stripall=True)
    #     formatter = HtmlFormatter()
    #     return highlight(html, lexer, formatter)

    # # Apply syntax highlighting to the HTML content
    # blog_html = highlight_code(blog_html)

    # Read the blog overview and add the HTML content to it
    with open(f"{blogs_folder}/{blog_id}/overview.json", "r") as f:
        overview = json.load(f)
    overview["content"] = blog_html
    return {"blog": overview}

if __name__ == "__main__":
    # Run the Flask application in debug mode
    app.run(debug=True)