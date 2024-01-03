from flask import Flask,render_template,request
from args import*
import numpy as np
import pickle
with open('Model.pkl','rb') as mod:
    model=pickle.load(mod)
with open('Scaler.pkl','rb') as mo:
    scaler=pickle.load(mo)
app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def index():
   # print(request.method)
   # print(request.form)
   if request.method=='POST':
          bathrooms=request.form['bathrooms']
          bedrooms=request.form['bedrooms']
          location=request.form['Location']
          sft=request.form['sft']
          status=request.form['Status']
          direction=request.form['direction']
          property_type=request.form['property_type_mapping']
          print(request.form)

          input_array=np.array([[bedrooms,bathrooms,location,sft,status,direction,property_type]])
          print('-------------------------------------------------')
          print(input_array)

          t_array=scaler.transform(input_array)

          prediction=model.predict(t_array)[0]

          return render_template('index.html',location_mapping=location_mapping,status_mapping =status_mapping,direction_mapping=direction_mapping,property_type_mapping=property_type_mapping,prediction=prediction)
   else:
          return render_template('index.html',location_mapping=location_mapping,status_mapping =status_mapping,direction_mapping=direction_mapping,property_type_mapping=property_type_mapping)
   
@app.route('/second')
def second():
    return 'I am in second page'
@app.route('/third')
def third():
    return 'I am third page'
if __name__=='__main__':
    #app.run(use_reloader=True,debug=True)
    app.run()

