from flask import Flask,render_template,url_for,request
import joblib
model=joblib.load('decisiontree.lb')

app=Flask(__name__)
@app.route('/')
def home():
    # return "my home page"
    return render_template('home.html')

@app.route('/prediction', methods=['GET','POST'])

def prediction():
    if request.method=='POST':
        brand=request.form['brand']
        spec_rating=int(request.form['spec_rating'])
        processor=request.form['processor']
        Ram=int(request.form['Ram'])
        Rom=int(request.form['ROM'])
        ROM_type=request.form['ROM_type']
        display_size=int(request.form['display_size'])
        resolution_width=int(request.form['resolution_width'])
        resolution_height=int(request.form['resolution_height'])
        warranty=int(request.form['warranty'])
        os=request.form['OS']
        CPU_Name=request.form['CPU Name']
        GPU_brand=request.form['GPU_brand']
        
        data=[[brand, spec_rating, processor, Ram, Rom, ROM_type,
       display_size, resolution_width, resolution_height, os,
       warranty, CPU_Name, GPU_brand]]
        prediction=model.predict(data)[0]
        print(prediction)
        return str(round(prediction[0],2))


#'brand', 'spec_rating', 'processor', 'Ram', 'ROM', 'ROM_type',
       #'display_size', 'resolution_width', 'resolution_height', 'OS',
       #'warranty', 'CPU Name', 'GPU_brand'




if __name__=="__main__":
    app.run(debug=True)