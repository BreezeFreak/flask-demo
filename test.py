from app import App  # 为什么无法用.app，编译器报错反而能运行

app = App.create_app()

if __name__ == "__main__":
    app.run(debug=app.config['DEBUG'], port=app.config['PORT'])
