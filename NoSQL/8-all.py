#!/usr/bin/env python3
"""
function that lists all documents in a collection
"""


def list_all_documents(mongo_collection):
    """
    listing documents
    """
    result = mongo_collection.school.find()
    return result if result else []
