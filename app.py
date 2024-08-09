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
   
    if request.method == 'POST':
        try:
            # Retrieve form data
            brand = request.form.get('brand', '')
            spec_rating = int(request.form.get('spec_rating', 0))
            processor = request.form.get('processor', '')
            Ram = int(request.form.get('Ram', 0))
            Rom = int(request.form.get('ROM', 0))  # Make sure 'ROM' exists in the form
            ROM_type = request.form.get('ROM_type', '')
            display_size = int(request.form.get('display_size', 0))
            resolution_width = int(request.form.get('resolution_width', 0))
            resolution_height = int(request.form.get('resolution_height', 0))
            warranty = int(request.form.get('warranty', 0))
            os = request.form.get('OS', '')
            CPU_Name = request.form.get('CPU Name', '')
            GPU_brand = request.form.get('GPU_brand', '')

            # Prepare data for prediction
            data = [[brand, spec_rating, processor, Ram, Rom, ROM_type,
                    display_size, resolution_width, resolution_height, os,
                    warranty, CPU_Name, GPU_brand]]

            # Predict
            prediction = model.predict(data)[0]
            return str(round(prediction, 2))

        except Exception as e:
            return str(e)  # Return the error message

    return render_template('home.html')

if __name__=="__main__":
    app.run(debug=True)