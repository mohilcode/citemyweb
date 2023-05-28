from flask import Flask, render_template, request, redirect, url_for
from citation_fetcher import get_citation
import os

def app():
    app = Flask(__name__)

    citations = []
    default_styles = {}

    @app.route("/")
    def index():
        has_citations = bool(citations)
        return render_template("index.html", citations=citations, has_citations=has_citations, default_style=default_styles.get('default'))

    @app.route("/citation", methods=["POST"])
    def citation():
        url = request.form["url"]
        style = request.form["style"]

        try:
            citation_text = get_citation(url, style)
        except ValueError as e:
            return render_template("index.html", citations=citations, error_message=str(e), default_style=default_styles.get('default'))

        citations.append(citation_text)
        return redirect(url_for('index'))

    @app.route("/default-style", methods=["POST"])
    def set_default_style():
        default_style = request.form["default_style"]
        default_styles['default'] = default_style
        return redirect(url_for('index'))

    return app

app = app()

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
