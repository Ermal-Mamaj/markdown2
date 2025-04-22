from markdown import markdown
from weasyprint import HTML
import os

def markdown_to_html(markdown_text: str) -> str:
    """Convert Markdown text to HTML."""
    return markdown(markdown_text, output_format='html5')

def html_to_pdf(html_content: str, output_path: str) -> None:
    """
    Convert HTML content to PDF and save it to the specified output_path.
    """
    # Ensure the output directory exists
    output_dir = os.path.dirname(output_path)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)

    # Write the PDF
    HTML(string=html_content).write_pdf(output_path)
