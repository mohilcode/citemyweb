from flask import Flask, render_template, request, redirect, url_for, session
from citation_fetcher import get_citation
import os

def app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.urandom(24)  # Secret key is necessary for sessions to work

    default_styles = {}

    @app.route("/")
    def index():
        citations = session.get('citations', [])  # Get the citations from the session (or an empty list if not set)
        has_citations = bool(citations)
        return render_template("index.html", citations=citations, has_citations=has_citations, default_style=default_styles.get('default'))

    @app.route("/citation", methods=["POST"])
    def citation():
        url = request.form["url"]
        style = request.form["style"]

        try:
            citation_text = get_citation(url, style)
        except ValueError as e:
            return render_template("index.html", citations=session.get('citations', []), error_message=str(e), default_style=default_styles.get('default'))

        # Get the current list of citations from the session, append the new citation, and then save it back to the session
        citations = session.get('citations', [])
        citations.append(citation_text)
        session['citations'] = citations

        return redirect(url_for('index'))


    return app

app = app()

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
