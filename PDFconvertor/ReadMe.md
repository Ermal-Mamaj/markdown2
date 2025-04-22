# Markdown to PDF Converter

This is a web application that allows you to upload a Markdown file, convert it to HTML, and then generate a PDF of the content with customizable themes. It is easy to use, and the app is fully containerized with Docker for consistent deployment.

 Features
- Upload a Markdown file to convert it to a styled PDF.
- Choose between different PDF themes like "article" and "resume."
- Simple drag-and-drop frontend interface.
- PDF generated with WeasyPrint and styled with CSS.

Technologies
- **Backend**: FastAPI
- **PDF Generation**: WeasyPrint
- **Styling**: CSS for HTML and PDF
- **Containerization**: Docker

     How to Use
 Option 1: Clone from GitHub

1. Clone this repository to your local machine:
   ```bash
     git clone https://github.com/Ermal-Mamaj/markdown2.git
     cd markdown2/pdfconvertor
     docker-compose up --build
