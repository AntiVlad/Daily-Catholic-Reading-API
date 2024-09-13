from flask import Flask, jsonify, make_response
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

app = Flask(__name__)

def get_formatted_date():

    gmt_plus_one = datetime.utcnow() + timedelta(hours=1)

    formatted_date = gmt_plus_one.strftime('%d%m%y')
    return formatted_date

def fetch_daily_readings():

    formatted_date = get_formatted_date()
    url = f'https://www.catholicgallery.org/mass-reading/{formatted_date}/?utm_source=www.catholicgallery.org&utm_medium=mrwidget'
    
    try:

        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        start_element = soup.select_one('#massrdgtop')
        end_element = soup.select_one('#massrdgfoot')

        elements_between = []
        current_element = start_element.find_next_sibling()
        
        while current_element and current_element != end_element:
            elements_between.append(current_element)
            current_element = current_element.find_next_sibling()
        for element in elements_between:
            for ins in element.find_all('ins'):
                ins.decompose()

        cleaned_html = ''.join(str(element) for element in elements_between)
        return cleaned_html
    
    except requests.RequestException as e:
        print(f'Error fetching daily readings: {e}')
        return None

@app.route('/daily-readings', methods=['GET'])
def daily_readings():
    html_content = fetch_daily_readings()
    if html_content:
        return make_response(html_content, 200)
    else:
        return make_response(jsonify({'error': 'An error occurred while fetching daily readings.'}), 500)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
