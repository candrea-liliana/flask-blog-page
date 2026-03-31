from flaskblog import app
from flaskblog import models

# Execute initialization with context
if __name__ == "__main__":
    app.run(debug=True)
    with app.app_context():
        models.init_db()