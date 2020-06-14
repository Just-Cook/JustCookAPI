from app_justcook import app, mngt

app.app_context().push()

def run():
    mngt.populate_db()

if __name__ == '__main__':
    run()
    print("done.")
