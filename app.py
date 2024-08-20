from flask import Flask,render_template,request
app = Flask(__name__,static_url_path='/static')
import pickle
import numpy as np

model = pickle.load(open('Airline Passenger.pkl','rb'))


@app.route('/')
def start():
    return render_template('index.html')

@app.route('/login',methods =['POST'])

def login():
   
   a = request.form["Gender"]
   if (a=="Female"):
       a=0
   else:
       a=1
    
   b = request.form["Customer Type"]
   if (b=="Loyal Customer"):
       b=0
   else:
       b=1
   c = request.form["Age"]
   d = request.form["Type of Travel"]
   if (d=="Personal Travel"):
       d=1
   else:
       d=0
   e = request.form["Class"]
   if (e=="Business"):
       e=0
   elif(e=="Eco"):
       e=1
   else:
       e=2 
   
   f = request.form["Flight Distance"]
   g = request.form["Inflight wifi service"]
   h = request.form["Departure/Arrival time convenient"]
   i = request.form["Ease of Online booking"]
   j = request.form["Gate location"]
   k = request.form["Food and drink"]
   l = request.form["Online boarding"]
   m = request.form["Seat comfort"]
   n = request.form["Inflight entertainment"]
   o = request.form["On-board service"]
   p = request.form["Leg room service"]
   q = request.form["Baggage handling"]
   r = request.form["Checkin service"]
   s = request.form["Inflight service"]
   t = request.form["Cleanliness"]
   u = request.form["Departure Delay in Minutes"]
   v = request.form["Arrival Delay in Minutes"]
   
   
   total =  [[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v]] 
   output =model.predict(total)
   if (output == 1):
       Prediction = "Satisfied"
   else:
       Prediction = "Neutral or dissatisfied" 

   return render_template("index.html", y = "The passenger  is  "+Prediction)

if __name__ == '__main__' :
    app.run(debug=True)