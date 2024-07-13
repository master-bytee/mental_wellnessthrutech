
from flask import Flask, render_template, request, redirect, url_for
import json
from datetime import datetime

app = Flask(__name__)

# Load mood data
def load_moods():
    try:
        with open('data/moods.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save mood data
def save_moods(moods):
    with open('data/moods.json', 'w') as file:
        json.dump(moods, file, indent=4)

# Load gratitude data
def load_gratitude():
    try:
        with open('data/gratitude.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save gratitude data
def save_gratitude(gratitude_entries):
    with open('data/gratitude.json', 'w') as file:
        json.dump(gratitude_entries, file, indent=4)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mood_tracker', methods=['GET', 'POST'])
def mood_tracker():
    if request.method == 'POST':
        mood = request.form['mood']
        moods = load_moods()
        moods.append({'date': datetime.now().strftime('%Y-%m-%d'), 'mood': mood})
        save_moods(moods)
        return redirect(url_for('mood_tracker'))
    return render_template('mood_tracker.html', moods=load_moods())

@app.route('/gratitude_journal', methods=['GET', 'POST'])
def gratitude_journal():
    if request.method == 'POST':
        entry = request.form['entry']
        gratitude_entries = load_gratitude()
        gratitude_entries.append({'date': datetime.now().strftime('%Y-%m-%d'), 'entry': entry})
        save_gratitude(gratitude_entries)
        return redirect(url_for('gratitude_journal'))
    return render_template('gratitude_journal.html', gratitude_entries=load_gratitude())


if __name__ == '__main__':
    app.run(debug=True)
