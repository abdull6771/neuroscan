# NeuroScan: AI-Powered Brain Tumor Classification

![NeuroScan Banner](static/test.png) 
*AI-driven brain tumor detection using MRI scans.*

## Overview

NeuroScan is a web-based application that leverages a TensorFlow Lite deep learning model to classify brain tumors from MRI images. Designed for medical professionals, researchers, and tech enthusiasts, it provides an intuitive interface to upload images, receive predictions, and explore AI-driven insights. Built with Flask and styled with Tailwind CSS, NeuroScan combines technical sophistication with a responsive, modern design.

Developed by Abdullahi Ahmad, a Huawei ICT Competition Grand Prize winner, NeuroScan aims to enhance early tumor detection, offering a scalable tool for healthcare innovation.

## Features

- **Brain Tumor Classifier**: Upload an MRI image to get instant predictions ("Tumor Detected" or "No Tumor") with confidence scores.
- **Interactive Demo Dashboard**: Analyze multiple images with prediction galleries and simulated heatmaps.
- **Tech & Insights**: Explore model details, performance metrics (e.g., 92% accuracy), and sample results.
- **Dataset Details**: Learn about the 400-image "Brain_Tumor_Images" dataset (170 Normal, 230 Tumor).
- **About the CEO**: Meet Abdullahi Ahmad, the visionary behind NeuroScan, with his custom profile image.
- **Responsive Design**: Gradient-themed UI with Tailwind CSS, optimized for all devices.
- **Additional Pages**: About, Contact, and more for a comprehensive experience.

## Dataset

The "Brain_Tumor_Images" dataset powers NeuroScan:
- **Total Images**: 400 MRI scans.
- **Categories**: Normal (170), Tumor (230).
- **Split**:
  - **Training**: 136 Normal, 184 Tumor (320 total).
  - **Validation**: 34 Normal, 46 Tumor (80 total).

## Installation

### Prerequisites
- Python 3.8–3.11
- Git
- A compatible environment (e.g., Anaconda, virtualenv)

### Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/abdull6771/neuroscan.git
   cd neuroscan
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   If `requirements.txt` isn’t present, install manually:
   ```bash
   pip install flask tensorflow pillow numpy
   ```

3. **Add Your Model**:
   - Place your `model.tflite` file in the project root (`neuroscan/`).

4. **Add CEO Image**:
   - Copy your `ceo.jpeg` to the `static/` folder:
     ```bash
     cp /path/to/ceo.jpeg static/
     ```

### Project Structure
```
neuroscan/
├── app.py              # Flask application
├── templates/          # HTML templates
│   ├── index.html
│   ├── about.html
│   ├── contact.html
│   ├── tech_insights.html
│   ├── demo_dashboard.html
│   ├── about_dataset.html
│   └── about_ceo.html
├── static/             # Static assets
│   └── ceo.jpeg
├── model.tflite        # TensorFlow Lite model (not included)
└── README.md
```

## Usage

1. **Run the Application**:
   ```bash
   python app.py
   ```

2. **Access the Web Interface**:
   - Open your browser to `http://127.0.0.1:5000/`.
   - Upload an MRI image on the home page to test the classifier.
   - Explore other pages via the navigation bar.

3. **Demo Dashboard**:
   - Visit `/demo_dashboard` to upload multiple images and view predictions with heatmaps.

## Technical Details

- **Backend**: Flask, TensorFlow Lite (CNN model).
- **Frontend**: Tailwind CSS via CDN, Jinja2 templating.
- **Image Processing**: PIL (Pillow) for resizing, NumPy for array operations, base64 for display.
- **Heatmaps**: Simulated by averaging RGB channels (placeholder for Grad-CAM).

## Contributing

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a branch: `git checkout -b feature/your-feature`.
3. Commit changes: `git commit -m "Add your feature"`.
4. Push to your fork: `git push origin feature/your-feature`.
5. Open a pull request.

## Future Enhancements

- Full Grad-CAM integration for precise heatmaps.
- RESTful API for third-party integration.
- Multi-class tumor classification.
- Cloud deployment (e.g., AWS, Azure).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details (add one if desired).

## Contact

- **Developer**: Abdullahi Ahmad
- **Email**: abdulll8392
- **GitHub**: [abdull6771](https://github.com/abdull6771)

---

*Built with passion for AI and healthcare innovation. Last updated: April 9, 2025.*
