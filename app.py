from flask import Flask, request, render_template
import tensorflow as tf
import numpy as np
from PIL import Image
import io
import base64

app = Flask(__name__)

# Load the TFLite model
interpreter = tf.lite.Interpreter(model_path="model.tflite")
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Image preprocessing function
def preprocess_image(image):
    img = image.resize((224, 224))
    img_array = np.array(img, dtype=np.float32)
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

# Simulate a heatmap (simplified approach)
def generate_heatmap(image):
    img_array = np.array(image.resize((224, 224)), dtype=np.float32) / 255.0
    heatmap = np.mean(img_array, axis=2)
    heatmap = (heatmap - heatmap.min()) / (heatmap.max() - heatmap.min())
    heatmap = (heatmap * 255).astype(np.uint8)
    heatmap_img = Image.fromarray(heatmap, mode='L')
    buffered = io.BytesIO()
    heatmap_img.save(buffered, format="PNG")
    heatmap_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')
    return heatmap_base64

# @app.route('/', methods=['GET', 'POST'])
# def upload_and_predict():
#     prediction = None
#     if request.method == 'POST':
#         if 'image' not in request.files:
#             return render_template('index.html', error="No file uploaded")
        
#         file = request.files['image']
#         if file.filename == '':
#             return render_template('index.html', error="No file selected")
        
#         if file:
#             try:
#                 image = Image.open(file.stream).convert('RGB')
#                 processed_image = preprocess_image(image)
                
#                 interpreter.set_tensor(input_details[0]['index'], processed_image)
#                 interpreter.invoke()
#                 output_data = interpreter.get_tensor(output_details[0]['index'])
                
#                 prediction_score = output_data[0][0]
#                 prediction = "Tumor Detected" if prediction_score > 0.5 else "No Tumor"
#                 confidence = f"{prediction_score*100:.2f}%" if prediction_score > 0.5 else f"{(1-prediction_score)*100:.2f}%"
                
#             except Exception as e:
#                 return render_template('index.html', error=f"Error processing image: {str(e)}")
    
#     return render_template('index.html', prediction=prediction, confidence=confidence)
@app.route('/', methods=['GET', 'POST'])
def upload_and_predict():
    prediction = None
    confidence = None  # Add this to avoid UnboundLocalError
    if request.method == 'POST':
        if 'image' not in request.files:
            return render_template('index.html', error="No file uploaded", prediction=prediction, confidence=confidence)
        
        file = request.files['image']
        if file.filename == '':
            return render_template('index.html', error="No file selected", prediction=prediction, confidence=confidence)
        
        if file:
            try:
                image = Image.open(file.stream).convert('RGB')
                processed_image = preprocess_image(image)
                
                interpreter.set_tensor(input_details[0]['index'], processed_image)
                interpreter.invoke()
                output_data = interpreter.get_tensor(output_details[0]['index'])
                
                prediction_score = output_data[0][0]
                prediction = "Tumor Detected" if prediction_score > 0.5 else "No Tumor"
                confidence = f"{prediction_score*100:.2f}%" if prediction_score > 0.5 else f"{(1-prediction_score)*100:.2f}%"
                
            except Exception as e:
                return render_template('index.html', error=f"Error processing image: {str(e)}", prediction=prediction, confidence=confidence)
    
    return render_template('index.html', prediction=prediction, confidence=confidence)
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/tech_insights')
def tech_insights():
    return render_template('tech_insights.html')

@app.route('/demo_dashboard', methods=['GET', 'POST'])
def demo_dashboard():
    results = []
    if request.method == 'POST':
        if 'images' not in request.files:
            return render_template('demo_dashboard.html', error="No files uploaded")
        
        files = request.files.getlist('images')
        for file in files:
            if file and file.filename:
                try:
                    image = Image.open(file.stream).convert('RGB')
                    processed_image = preprocess_image(image)
                    
                    interpreter.set_tensor(input_details[0]['index'], processed_image)
                    interpreter.invoke()
                    output_data = interpreter.get_tensor(output_details[0]['index'])
                    
                    prediction_score = output_data[0][0]
                    prediction = "Tumor Detected" if prediction_score > 0.5 else "No Tumor"
                    confidence = f"{prediction_score*100:.2f}%" if prediction_score > 0.5 else f"{(1-prediction_score)*100:.2f}%"
                    
                    buffered = io.BytesIO()
                    image.resize((224, 224)).save(buffered, format="PNG")
                    img_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')
                    
                    heatmap_base64 = generate_heatmap(image)
                    
                    results.append({
                        'image': img_base64,
                        'heatmap': heatmap_base64,
                        'prediction': prediction,
                        'confidence': confidence
                    })
                except Exception as e:
                    return render_template('demo_dashboard.html', error=f"Error processing image: {str(e)}")
    
    return render_template('demo_dashboard.html', results=results)

@app.route('/about_dataset')
def about_dataset():
    return render_template('about_dataset.html')

@app.route('/about_ceo')
def about_ceo():
    return render_template('about_ceo.html')

if __name__ == '__main__':
    app.run(debug=True)