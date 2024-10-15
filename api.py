from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/search-datasets', methods=['GET'])
def search_datasets():
    response = requests.get('https://huggingface.co/api/datasets')
    datasets = response.json()
    
    relevant_details = []
    for dataset in datasets:
        relevant_details.append({
            'id': dataset['id'],
            'author': dataset['author'],
            'description': dataset['description'][:200] + '...' if len(dataset['description']) > 200 else dataset['description'],
            'downloads': dataset['downloads'],
            'likes': dataset['likes'],
            'tags': dataset['tags']
        })
    
    return jsonify(relevant_details)

# Add more routes for preprocessing, model selection, and finetuning

if __name__ == '__main__':
    app.run(debug=True)
