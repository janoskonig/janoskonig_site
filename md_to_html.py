import markdown
import os

input_folder = 'blog'
output_folder = 'generated'
blog_index_file = 'blog.html'

# HTML wrappers
header_html = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{title}</title>
  <link rel="stylesheet" href="../style.css">
</head>
<body>
  <nav>
    <a href="../index.html">Home</a>
    <a href="../blog.html">Blog</a>
    <a href="../teaching.html">Teaching</a>
    <a href="../contact.html">Contact</a>
  </nav>
  <main>
'''

footer_html = '''
  </main>
  <footer>
    <p>&copy; 2025 Your Name</p>
  </footer>
</body>
</html>
'''

blog_index_header = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Blog</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <nav>
    <a href="index.html">Home</a>
    <a href="blog.html">Blog</a>
    <a href="teaching.html">Teaching</a>
    <a href="contact.html">Contact</a>
  </nav>
  <main>
    <h1>Blog</h1>
    <ul>
'''

blog_index_footer = '''
    </ul>
  </main>
  <footer>
    <p>&copy; 2025 Your Name</p>
  </footer>
</body>
</html>
'''

# Prepare folders
os.makedirs(output_folder, exist_ok=True)

# Collect blog post data
posts = []

for filename in os.listdir(input_folder):
    if filename.endswith('.md'):
        md_path = os.path.join(input_folder, filename)
        with open(md_path, 'r', encoding='utf-8') as f:
            md_text = f.read()
            html_body = markdown.markdown(md_text)

        # Get title from first line
        title_line = md_text.strip().split('\n')[0]
        title = title_line.replace('# ', '').strip()

        html_content = header_html.format(title=title) + html_body + footer_html
        out_filename = filename.replace('.md', '.html')
        out_path = os.path.join(output_folder, out_filename)

        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(html_content)

        # Collect for index
        posts.append((title, f"{output_folder}/{out_filename}"))

# Generate blog.html index
with open(blog_index_file, 'w', encoding='utf-8') as f:
    f.write(blog_index_header)
    for title, path in sorted(posts):
        relative_path = path.replace('\\', '/')
        f.write(f'      <li><a href="{relative_path}">{title}</a></li>\n')
    f.write(blog_index_footer)

print("All markdown converted, blog.html index updated.")