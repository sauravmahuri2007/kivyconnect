from kivyserver import app

# Note: If want to serve this app using uwsgi, exeucte following command:
# uwsgi --socket 127.0.0.1:5000 --protocol=http -w wsgiserver:app

if __name__ == '__main__':
    app.run()

