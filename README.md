<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Project README</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
        }

        .container {
            width: 80%;
            margin: auto;
            overflow: hidden;
            padding: 20px;
        }

        h1, h2 {
            color: #333;
        }

        pre {
            background-color: #eee;
            border: 1px solid #ddd;
            padding: 10px;
            overflow-x: auto;
        }

        code {
            background-color: #f4f4f4;
            padding: 2px 4px;
            border-radius: 4px;
        }

        ul, ol {
            margin: 20px 0;
            padding: 0 20px;
        }

        ul li, ol li {
            margin: 10px 0;
        }

        a {
            color: #1a73e8;
            text-decoration: none;
        }

        a:hover {
            text-decoration: underline;
        }
    </style>

</head>
<body>
    <div class="container">
        <h1>Installation</h1>
        
        <h2>1. Clone the Repository</h2>
        <pre><code>git clone https://github.com/yourusername/your-repository-name.git
cd your-repository-name</code></pre>
        
        <h2>2. Set Up a Virtual Environment (optional but recommended)</h2>
        <p>On Unix or macOS:</p>
        <pre><code>python -m venv venv
source venv/bin/activate</code></pre>
        <p>On Windows:</p>
        <pre><code>python -m venv venv
venv\Scripts\activate</code></pre>
        
        <h2>3. Install Dependencies</h2>
        <pre><code>pip install -r requirements.txt</code></pre>
        
        <h1>Usage</h1>
        
        <h2>1. Run the Application Locally</h2>
        <p>Make sure to set your Anthropic API key in the script or as an environment variable.</p>
        <pre><code>streamlit run app.py</code></pre>
        
        <h1>Deployment</h1>
        
        <h2>Streamlit Community Cloud</h2>
        <ul>
            <li>Push your code to a GitHub repository.</li>
            <li>Go to <a href="https://share.streamlit.io/">Streamlit Community Cloud</a>.</li>
            <li>Click on “New app” and connect your GitHub account.</li>
            <li>Select your repository and deploy.</li>
        </ul>
        
        <h2>Heroku</h2>
        <ol>
            <li><strong>Create a <code>Procfile</code> with the following content:</strong>
                <pre><code>web: streamlit run app.py</code></pre>
            </li>
            <li><strong>Create a new Heroku app:</strong>
                <pre><code>heroku create your-app-name</code></pre>
            </li>
            <li><strong>Push your code to Heroku:</strong>
                <pre><code>git push heroku main</code></pre>
            </li>
            <li><strong>Open your app:</strong>
                <pre><code>heroku open</code></pre>
            </li>
        </ol>
    </div>
</body>
</html>
