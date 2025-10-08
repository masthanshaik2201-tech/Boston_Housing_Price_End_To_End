# Boston Housing Price Prediction

This repository contains an end-to-end Machine Learning project that predicts housing prices in Boston based on various input parameters such as the number of rooms, location, and crime rate. The project demonstrates how to train a model, integrate it into a Flask web application, and deploy it on Render using Gunicorn.

---

### 1. Software and Tools Required

1. [GitHub Account](https://github.com)
2. [VS Code IDE](https://code.visualstudio.com/)
3. [Render Account](https://render.com)
4. [Git CLI](https://git-scm.com/book/en/v2/Getting-Started-The-Command-Line)
5. [Anaconda (optional)](https://www.anaconda.com/) - for managing virtual environments

---

### 2. Create a New Environment

If using Anaconda:
```bash
conda create -p venv python==3.7 -y
conda activate venv/
```
If using Python virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```

### 3. Install Dependencies

Install all required dependencies from the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

### 4. Model Building
The Jupyter notebook file `Boston_House_price_End_to_End.ipynb` includes the following steps:

- Data loading and cleaning  
- Feature scaling and preprocessing  
- Model training (using algorithms such as Linear Regression)  
- Model evaluation  
- Saving the model and scaler as pickle files (`regmodel.pkl` and `scaling.pkl`)

### 5. Flask Web Application

The Flask app (`app.py`) serves as the interface between users and the trained model.

**Key features:**

- Takes input parameters from an HTML form  
- Loads the pre-trained model and scaler  
- Returns the predicted house price on the webpage  

All HTML files used for the web interface are stored inside the `templates/` directory.

### 6. Deployment on Render

Follow these steps to deploy the application on Render:

1. Push your project to GitHub.
2. Go to [Render Dashboard](https://dashboard.render.com/).
3. Click **New Web Service** and connect your GitHub repository.
4. Configure the settings as follows:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
5. Add any required environment variables in the Render Dashboard.
6. Click **Deploy** and wait for Render to build and launch your application.

Once deployed, Render will provide a live URL for your web application.

### 7. Project Structure
```bash
.
├── templates/                  # HTML templates for the web interface
├── .gitignore
├── Boston_House_price_End_to_End.ipynb   # Model training and analysis
├── LICENSE
├── Procfile                    # Defines the start command for deployment
├── README.md                   # Project documentation
├── app.py                      # Flask application script
├── regmodel.pkl                # Trained machine learning model
├── scaling.pkl                 # Scaler used for input normalization
├── requirements.txt            # Python dependencies
```
### 8. Environment Variables

If your application requires secrets or API keys, define them in Render's Environment Variables section.

Example:

| Variable Name | Description |
|---------------|-------------|
| `SECRET_KEY` | Flask secret key (optional) |
| `DATABASE_URL` | Database connection string (if applicable) |

### 9. Running the Application Locally
To run the application on your local system, use the following command:
``` bash
python app.py
```
Then, open your browser and visit:
[python.app.py](http://127.0.0.1:5000/)


### 10. Live Demo
Once deployed, your live app can be accessed here:
[HousePricePredictionapp](https://boston-housing-price-end-to-end.onrender.com)
