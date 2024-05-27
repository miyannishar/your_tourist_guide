# README

## Your Tour Guide

This project is a simple web application built with Streamlit and Langchain that helps users find major tourist attractions in the capital city of a selected country. 

### Features
- Select a country from the sidebar.
- Get the capital city of the selected country.
- Get the top 5 major tourist attractions in the capital city.

### Prerequisites

Before you begin, ensure you have met the following requirements:
- You have installed Python 3.x.
- You have a basic understanding of Python and Streamlit.
- You have an OpenAI API key.

### Installation

1. **Clone the Repository**
    ```bash
    git clone https://github.com/yourusername/your-tour-guide.git
    cd your-tour-guide
    ```

2. **Create a Virtual Environment**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the Required Packages**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up Environment Variables**
    Create a `.env` file in the root directory and add your OpenAI API key:
    ```
    OPENAI_API_KEY=your_openai_api_key
    ```

### Running the App

1. **Run the Streamlit App**
    ```bash
    streamlit run main.py
    ```

2. **Using the App**
    - Open your browser and navigate to the URL provided by the Streamlit output.
    - Use the sidebar to select a country.
    - The app will display the capital city and top 5 tourist attractions in that city.

### Code Overview

#### main.py
This file contains the main Streamlit app code:
- The app's title is set using `st.title`.
- A country is selected using `st.sidebar.selectbox`.
- If a country is selected, the `langchain_helper.generate_attraction_in_capital` function is called to get the capital city and major tourist attractions.
- The results are displayed in the Streamlit app using `st.header` and `st.write`.

#### langchain_helper.py
This file contains the function to generate tourist attractions:
- The OpenAI API key is loaded from environment variables.
- Two prompt templates are defined using `PromptTemplate` to get the capital city and tourist attractions.
- A sequential chain of these prompts is created using `SequentialChain`.
- The function `generate_attraction_in_capital` takes a country as input and returns the capital city and major attractions.

### License

This project is licensed under the MIT License. See the LICENSE file for more details.

### Contributing

To contribute to this project, please fork the repository and create a pull request. For major changes, please open an issue first to discuss what you would like to change.

### Contact

If you have any questions or suggestions, feel free to open an issue or contact on miyannishar786@gmail.com.

---

This README provides a comprehensive overview of the project, instructions for installation and running the app, and a brief description of the code structure.