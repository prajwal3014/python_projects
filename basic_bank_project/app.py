from flask import Flask, render_template, request
from db import get_balance, check_acc, update_balance

app = Flask(__name__)
app.secret_key = "GRIP BANK PROJECT BY PRAJWAL SHARMA"

@app.route('/')
def index() :
    return render_template('index.html')

@app.route('/to_customers_list', methods = ['GET', 'POST'])
def customers_list() :
    return render_template('customers_list.html')

@app.route('/to_transaction_from_details', methods = ['GET', 'POST'])
def to_transaction_from() :
    acc_no = request.form['btn']
    return render_template('transaction.html', acc = acc_no)

@app.route('/to_transaction')
def transactions() :
    return render_template('transaction.html')

@app.route('/to_prajwal', methods = ['GET', 'POST'])
def to_prajwal() :
    money = get_balance("prajwal@1")
    return render_template('details.html', name = "Prajwal Sharma", mail = "prajwalsharma@gmail.com", mobile = "8860300923", account = "prajwal@1", type = "Current", balance = str(money), img = "../static/me.jpg")

@app.route('/to_ayush', methods = ['GET', 'POST'])
def to_ayush() :
    money = get_balance("ayush@2")
    return render_template('details.html', name = "Ayush Rana", mail = "ayushrana@gmail.com", mobile = "9856124589", account = "ayush@2", type = "Current", balance = str(money), img = "../static/02.jpg")

@app.route('/to_harshit', methods = ['GET', 'POST'])
def to_harshit() :
    money = get_balance("harshit@3")
    return render_template('details.html', name = "Harshit Srivastava", mail = "harshitsrivastava@gmail.com", mobile = "8561429375", account = "harshit@3", type = "Current", balance = str(money), img = "../static/03.jpg")

@app.route('/to_parv', methods = ['GET', 'POST'])
def to_parv() :
    money = get_balance("parv@4")
    return render_template('details.html', name = "Parv Arora", mail = "parvarora@gmail.com", mobile = "8943615726", account = "parv@4", type = "Current", balance = str(money), img = "../static/04.jpg")

@app.route('/to_ankit', methods = ['GET', 'POST'])
def to_ankit() :
    money = get_balance("ankit@5")
    return render_template('details.html', name = "Ankit Luthra", mail = "ankitluthra@gmail.com", mobile = "9264351879", account = "ankit@5", type = "Current", balance = str(money), img = "../static/05.jpg")

@app.route('/to_aryan', methods = ['GET', 'POST'])
def to_aryan() :
    money = get_balance("aryan@6")
    return render_template('details.html', name = "Aryan Anand", mail = "aryananand@gmail.com", mobile = "7651234892", account = "aryan@6", type = "Current", balance = str(money), img = "../static/06.jpg")

@app.route('/to_shubam', methods = ['GET', 'POST'])
def to_shubam() :
    money = get_balance("shubam@7")
    return render_template('details.html', name = "Shubam Khandelwal", mail = "shubamkhandelwal@gmail.com", mobile = "9613457826", account = "shubam@7", type = "Current", balance = str(money), img = "../static/07.jpg")

@app.route('/to_arihant', methods = ['GET', 'POST'])
def to_arihant() :
    money = get_balance("arihant@8")
    return render_template('details.html', name = "Arihant Jain", mail = "arihantjain@gmail.com", mobile = "8231469257", account = "arihant@8", type = "Current", balance = str(money), img = "../static/08.jpg")

@app.route('/to_bhagyansh', methods = ['GET', 'POST'])
def to_bhagyansh() :
    money = get_balance("bhagyansh@9")
    return render_template('details.html', name = "Bhagyansh Kumar", mail = "bhagyanshkumar@gmail.com", mobile = "7516349826", account = "bhagyansh@9", type = "Current", balance = str(money), img = "../static/09.jpg")

@app.route('/to_rohit', methods = ['GET', 'POST'])
def to_rohit() :
    money = get_balance("rohit@10")
    return render_template('details.html', name = "Rohit Kumar", mail = "rohitkumar@gmail.com", mobile = "6214537892", account = "rohit@10", type = "Current", balance = str(money), img = "../static/10.jpg")

@app.route('/transaction', methods = ['GET', 'POST'])
def transaction() :
    sender = request.form.get('sender_acc')
    reciever = request.form.get('reciever_acc')
    amount = request.form.get('amount')
    
    acc_list = check_acc()

    if (sender not in acc_list) or (reciever not in acc_list) :
        return render_template('transaction.html', msg = "Wrong sender's or reciver's account number...!")
    else :
        s_balance = get_balance(sender)
        r_balance = get_balance(reciever)
        if int(amount) > int(s_balance) :
            return render_template('transaction.html', msg = "Not enough balance in sender's account...!")
        else :
            s_balance = int(s_balance) - int(amount)
            r_balance = int(r_balance) + int(amount)
            update_balance(s_balance, sender)
            update_balance(r_balance, reciever)
            return render_template('transaction.html', msg = "Money sent successfully...!")

#Main Function
if __name__ == "__main__" :
    app.run(debug=True)