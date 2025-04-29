from markdown import markdown
from weasyprint import HTML, CSS
import os

THEME_CSS_PATHS = {
    "default": "utils/css/default.css",
    "resume": "utils/css/resume.css",
    "article": "utils/css/article.css"
}

def markdown_to_html(markdown_text: str) -> str:
    return markdown(
        markdown_text, 
        output_format='html5',
        extensions=['extra', 'tables', 'toc']
    )

def html_to_pdf(html_content: str, output_path: str, theme: str = "default") -> None:

    output_dir = os.path.dirname(output_path)
    os.makedirs(output_dir, exist_ok=True)

    css_path = 'static/style.css'
    
    HTML(string=html_content).write_pdf(
        output_path,
        stylesheets=[CSS(filename=css_path)]
    )
