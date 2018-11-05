import requests
from flask import Flask, render_template, request
app = Flask(__name__)

# Endpoint for all available jobs
@app.route('/')
def postings():
    url = 'https://jobs.github.com/positions.json'
    r = requests.get(url).json()
    jobs = []
    for json in r:
        curr_job = {
            'description': json['description'],
            'location': json['location'],
            'title': json['title'],
            'type': json['type'],
            'company': json['company'],
            'link': json['url']
        }
        jobs.append(curr_job)
    return render_template('postings.html', jobs=jobs)

# Endpoint for search results
@app.route('/results', methods=['POST'])
def results():
    url = 'https://jobs.github.com/positions.json'
    title = request.form['title']
    location = request.form['location']
    r = requests.get(url).json()
    jobs = []
    for json in r:
        if (title.lower() in json['title'].lower() or json['title'].lower() in title.lower()) and (location.lower() in json['location'].lower() or json['location'].lower() in location.lower()):
            curr_job = {
                'description': json['description'],
                'location': json['location'],
                'title': json['title'],
                'type': json['type'],
                'company': json['company'],
                'link': json['url']
            }
            jobs.append(curr_job)
    return render_template('postings.html', jobs=jobs)  # title=title, location=location)


if __name__ == '__main__':
    app.run(debug=True)
