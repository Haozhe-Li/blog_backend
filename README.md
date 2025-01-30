# Blog Backend for JuiCy Water Studio

A quick setup guide to help you upload your first blog!

### Installation

1. Clone the repository.
2. Install the dependencies.
3. Start the application using `python3 app.py`.

### Uploading a Blog

1. First, create a new folder under the `/blogs` directory. You can name this folder whatever you want, but the name of the folder MUST be the same as the article `id` mentioned later.

2. Create a `markdown` file called `content.md` and write your blog in this file. Refer to the [Markdown Guide](https://www.markdownguide.org) for syntax details.

3. Upload your cover image to this folder.

4. Create an `overview.json` file with the following structure:
   ````json
   {
       "title": "Title of your blog",
       "description": "A brief description",
       "date": "Date in YYYY-MM-DD format, e.g., 2025-01-29",
       "author": "Author's name",
       "id": "IMPORTANT! THIS MUST BE THE SAME AS THE NAME OF THE FOLDER MENTIONED EARLIER",
       "cover": "Cover image file name, e.g., cover.webp"
   }
   ````

5. The structure should look like this:
   ```
   blogs/
       your_blog_id/
           content.md
           overview.json
           cover.webp
   ```

6. Once finished, `git push` your changes. The blog will be automatically deployed and served.


### Acknowledgements

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.