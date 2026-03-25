from app import create_app

app = create_app()

if __name__ == "__main__":
    try:
        app.run(debug=True, port=3333)
    finally:
        print('Server Already: http://localhost:3333')