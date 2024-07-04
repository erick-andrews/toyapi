from flask import Flask, request, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os

app = Flask(__name__)

@app.route('/top-tweet', methods=['POST'])
def get_top_tweet():
    data = request.get_json()
    username = data.get('username')

    if not username:
        return jsonify({'error': 'Username is required'}), 400

    # Set up Selenium and ChromeDriver
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=ChromeService(executable_path="/usr/bin/chromedriver"), options=chrome_options)
    
    try:
        driver.get(f"https://twitter.com/{username}")
        top_tweet = driver.find_element(By.XPATH, '//div[@data-testid="tweet"]//span').text
        driver.quit()
        return jsonify({'username': username, 'top_tweet': top_tweet}), 200
    except Exception as e:
        driver.quit()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)