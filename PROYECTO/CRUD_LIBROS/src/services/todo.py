from flask import request, Response
from bson import json_util, ObjectId

from config.mongodb import mongo

def create_todo_service():
    data = request.get_json()
    title = data.get('title', None)
    author = data.get('author', None)
    genre = data.get('genre', None)
    publication_date = data.get('publication_date', None)

    # Validación de fecha
    try:
        from datetime import datetime
        datetime.strptime(publication_date, "%Y-%m-%d")
    except ValueError:
        return {'error': 'Formato de fecha inválido. Use el formato AAAA-MM-DD'}, 400

    if title and author and genre and publication_date:
        book = {
            'title': title,
            'author': author,
            'genre': genre,
            'publication_date': publication_date
        }
        mongo.db.books.insert_one(book)
        return {'message': 'Libro creado exitosamente'}
    else:
        return {'error': 'Algo salió mal'}, 400
    
def get_todos_service():
    books = mongo.db.books.find()
    result = json_util.dumps(books)
    return Response(result, mimetype='application/json')

def get_todo_service(id):
    book = mongo.db.books.find_one({'_id': ObjectId(id)})
    result = json_util.dumps(book)
    return Response(result, mimetype='application/json')

def update_todo_service(id):
    books = request.get_json()
    if len(books) == 0:
        return {'error': 'Ingreso no valido'}, 400
    
    response = mongo.db.books.update_one({'_id': ObjectId(id)}, {'$set': books})

    if response.modified_count > 0:
        return {'message': 'Libro actualizado exitosamente'}
    else:
        return {'error': 'No se encontró el libro'}, 400
    
def delete_todo_service(id):
    response = mongo.db.books.delete_one({'_id': ObjectId(id)})
    if response.deleted_count > 0:
        return {'message': 'Libro eliminado exitosamente'}
    else:
        return {'error': 'No se encontró el libro'}, 400