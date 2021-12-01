from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = "GRIP BANK PROJECT BY PRAJWAL SHARMA"

@app.route('/')
def index() :
    return render_template('index.html')

@app.route('/to_customers_list')
def customers_list() :
    return render_template('customers_list.html')

@app.route('/to_transaction')
def transactions() :
    return render_template('index.html')

if __name__ == "__main__" :
    app.run(debug=True)