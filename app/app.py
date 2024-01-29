from flask import Flask, render_template, request, jsonify, Response
import requests

app = Flask(__name__)


# books_api_url = os.environ.get('BOOKS_API_URL')
books_api_url = 'http://book-api-server-sse-lab-10.g9hrggepb6h5dxgy.uksouth.azurecontainer.io:5000/book'


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/book-search", methods=['GET'])
def search_books():
    query_type = request.args.get('queryType')
    filter_value = request.args.get('filterValue')
    
    # Construct the query string based on the query type
    query_string = ''
    if query_type == 'genre':
        query_string = f'?genre={filter_value.lower()}'
    elif query_type == 'author':
        query_string = f'?author={filter_value.lower()}'
    
    # Make a GET request to the API server with the appropriate query string
    response = requests.get(f"{books_api_url}{query_string}")
    
    # Check if the request was successful
    if response.status_code == 200 or response.status_code == 404:
        books_data = response.json()
        return render_template("index.html", books_data=books_data)
    else:
        # Handle errors
        error_message = 'Could not retrieve data from the books API'
        return render_template("index.html", error_message=error_message)



@app.route("/books", methods=['GET'])
def callBooksApi():
    # Retrieve genre or author from the query parameters
    genre = request.args.get('genre')
    author = request.args.get('author')
    
    # Construct the query string based on the provided parameters
    query_string = ''
    if genre:
        query_string = f'?genre={genre.lower()}'
    elif author:
        query_string = f'?author={author.lower()}'
    
    # Make a GET request to the API server with the appropriate query string
    response = requests.get(f"{books_api_url}{query_string}")
    
    # Check if the request was successful
    if response.status_code == 200:
        books_data = response.json()
        return jsonify(books_data)
    else:
        # Handle errors
        return jsonify({'error': 'Could not retrieve data from the books API'}), response.status_code



if __name__ == "__main__":
    app.run()
    app.run(host='127.0.0.1', port=5002)

