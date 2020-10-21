from google.cloud import firestore
from datetime import datetime, timezone, timedelta

db = firestore.Client()


def get_document_name(name_collection, name_document):
    print(f'Get document {name_document} in {name_collection}')
    data = None
    doc = db.collection(name_collection).document(name_document).get()
    data = doc.to_dict()
    return data


def get_document_filter(name_collection, name_filter, value_filter):
    print(f'Get document {name_filter}|{value_filter} in {name_collection}')
    data = []
    docs = db.collection(name_collection).where(
        name_filter, '==', value_filter).get()
    for doc in docs:
        data.append(doc.to_dict())
    return data


def set_document(name_collection, name_document, data):
    date = datetime.utcnow()
    timestamp = int(date.replace(tzinfo=timezone.utc).timestamp())
    iso_date = date.isoformat()
    data['updatedAtISO'] = firestore.SERVER_TIMESTAMP
    db.collection(name_collection).document(
        name_document).set(data)
    print(
        f'Creater document {name_document} in {name_collection}, data: {data}')

    return True


def update_document(name_collection, name_document, data):
    date = datetime.utcnow()
    timestamp = int(date.replace(tzinfo=timezone.utc).timestamp())
    iso_date = date.isoformat()
    data['updated_at'] = firestore.SERVER_TIMESTAMP
    db.collection(name_collection).document(name_document).update(data)
    print(
        f'Updated document {name_document} in {name_collection}, data: {data}')

    return True


# print(len(get_document_filter("fc_belgingur",
#                               "forecastDate", "2020-10-15T03:00:00+00:00")))
