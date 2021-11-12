import json
from urllib.parse import unquote

from flask import current_app as app
from flask import request

from .document_service import make_summary
from .models import DocumentModel, db


@app.route("/doc", methods=["POST"])
def add_document():
    """
    Add document with generated summary
    """
    doc_text = unquote(request.form["text"])
    if doc_text:
        doc_summary = make_summary(doc_text)
        new_doc = DocumentModel(body=doc_text, summary=doc_summary)
        db.session.add(new_doc)
        db.session.commit()
        payload = {"document_id": new_doc.id}

        return (
            payload,
            201,
            {"Content-Type": "application/json"},
        )

    else:
        return (
            json.dumps({"error": "No text provided"}),
            400,
            {"Content-Type": "application/json"},
        )


@app.route("/doc/<int:doc_id>", methods=["GET"])
def get_document(doc_id):
    """
    Get document with given id
    """
    doc = DocumentModel.query.get_or_404(doc_id)

    payload = {
        "document_id": doc.id,
        "summary": doc.summary,
    }

    return payload, 200, {"Content-Type": "application/json"}
