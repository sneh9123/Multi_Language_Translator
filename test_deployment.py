import requests
import time

def test_flask_app():
    """Test if the Flask app is running and accessible"""
    try:
        # Wait a moment for the app to start
        time.sleep(2)
        
        # Test the home page
        response = requests.get('http://localhost:5000', timeout=5)
        if response.status_code == 200:
            print("✅ Flask app is running successfully!")
            print(f"Status Code: {response.status_code}")
            print("🌐 You can access your app at: http://localhost:5000")
            return True
        else:
            print(f"❌ Flask app returned status code: {response.status_code}")
            return False
            
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to Flask app. Make sure it's running.")
        return False
    except Exception as e:
        print(f"❌ Error testing Flask app: {e}")
        return False

if __name__ == "__main__":
    print("🧪 Testing Flask app deployment...")
    test_flask_app() 