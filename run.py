from app_justcook import app, db



@app.shell_context_processor
def shell_context():
    return dict(
        app=app,
        db=db
    )


if __name__ == '__main__':
    app.run(debug=True, port=5000, host="0.0.0.0")
