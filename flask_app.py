from flask import Flask
app=Flask(__name__)

# Hieronder code invoeren

@app.route('/')
def home():
    return "Hello World"




# Hierboven code invoeren

if __name__ == '__main__':
    app.run(port=5000, debug=True)