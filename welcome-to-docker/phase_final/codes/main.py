import json
from flask import Flask, abort, request, jsonify

# Import services while avoiding potential namespace conflicts by using explicit names
from elasticHelper import ElasticSearchService
from redisHelper import RedisCacheSystem
from imdb import imdb  

app = Flask(__name__)

# Initialize Redis and Elasticsearch services outside the main block
cache_system = RedisCacheSystem()
search_system = ElasticSearchService()

@app.route('/search', methods=['GET'])
def search():
    # Extract 'query' from the request parameters
    query = request.args.get('query')
    if not query:
        # Return a 400 Bad Request error if no query parameter is provided
        return abort(400, {'message': 'Bad request due to missing query parameter.'})
    
    try:
        # Attempt to retrieve data from the Redis cache
        redis_info = cache_system.find(query)
        if redis_info:
            # If data exists in Redis, parse it from JSON and return it
            return jsonify({
                'result': json.loads(redis_info), 
                'message': "Data retrieved from Redis cache."
            })

        # Data not found in Redis; proceed to search in Elasticsearch
        print("Data not found in Redis; searching in Elasticsearch.")
        elasticsearch_info = search_system.search(query)
        if elasticsearch_info:
            # Cache and return the Elasticsearch data if found
            cache_system.add(query, json.dumps(elasticsearch_info))
            return jsonify({
                'result': elasticsearch_info,
                'message': "Data retrieved from Elasticsearch service."
            })

        # If data is not found in Elasticsearch, use the imdb search service
        print("Data not found in Elasticsearch; querying imdb search service.")
        api_info = imdb(query)
        if api_info:
            # Cache and return the data from the imdb search service if found
            cache_system.add(query, json.dumps(api_info))
            return jsonify({
                'result': api_info, 
                'message': "Data retrieved from imdb search API service."
            })

        # If no data is found across all services, return a 404 Not Found error
        return abort(404, {'message': 'No results found across all data sources.'})

    except Exception as e:
        # Handle unexpected errors and return a 500 Internal Server Error
        print(f"An error occurred: {e}")
        return abort(500, {'message': f"Server error processing the request. {e}"})

if __name__ == '__main__':
    # Configure Flask app to run on all interfaces with debugging turned off
    app.run(debug=False, host='0.0.0.0', port=5000)
