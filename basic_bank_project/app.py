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
    return render_template('transaction.html')

@app.route('/to_prajwal', methods = ['GET', 'POST'])
def to_prajwal() :
    return render_template('prajwal.html')

@app.route('/to_ayush', methods = ['GET', 'POST'])
def to_ayush() :
    return render_template('ayush.html')

@app.route('/to_harshit', methods = ['GET', 'POST'])
def to_harshit() :
    return render_template('harshit.html')

@app.route('/to_parv', methods = ['GET', 'POST'])
def to_parv() :
    return render_template('parv.html')

@app.route('/to_ankit', methods = ['GET', 'POST'])
def to_ankit() :
    return render_template('ankit.html')

@app.route('/to_aryan', methods = ['GET', 'POST'])
def to_aryan() :
    return render_template('aryan.html')

@app.route('/to_shubam', methods = ['GET', 'POST'])
def to_shubam() :
    return render_template('shubam.html')

@app.route('/to_arihant', methods = ['GET', 'POST'])
def to_arihant() :
    return render_template('arihant.html')

@app.route('/to_bhagyansh', methods = ['GET', 'POST'])
def to_bhagyansh() :
    return render_template('bhagyansh.html')

@app.route('/to_rohit', methods = ['GET', 'POST'])
def to_rohit() :
    return render_template('rohit.html')

if __name__ == "__main__" :
    app.run(debug=True)