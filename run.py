from flaskblog import create_app

app = create_app()

# Execute initialization with context
if __name__ == "__main__":
    app.run(debug=True)