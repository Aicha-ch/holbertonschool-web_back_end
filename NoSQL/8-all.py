#!/usr/bin/env python3
"""
function that lists all documents in a collection
"""


def list_all_documents(mongo_collection):
    """
    list docs
    """
    result = mongo_collection.school.find()
    if result:
        return result
    return []

