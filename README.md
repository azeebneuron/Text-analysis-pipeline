# Text-analysis-pipeline
This repository contains a comprehensive text analysis pipeline developed in Python for extracting insights from a collection of URLs.


### extraction.py
The extraction.py script is responsible for extracting text content from a list of URLs. It handles cases where 404 errors are encountered and generates an error log containing the URLs with 404 errors.

### Running extraction.py:

1. **Install Python**: Ensure you have Python installed on your system. If not, download and install the latest version of Python.

2. **Open Terminal/Command Prompt**: Launch your terminal or command prompt.

3. **Navigate to File Directory**: Use the `cd` command to navigate to the directory where the `extraction.py` file is located.

4. **Execute Script**: Run the script by entering the following command:
   ```
   python extraction.py
   ```
   
5. **Complete Execution**: Allow the script to complete the data extraction process. Make sure all necessary dependencies are installed prior to execution.

### analysis.py
The analysis.py script utilizes the extracted text data to perform sentiment analysis, calculate readability metrics, and generate an output Excel file with insightful metrics for further analysis.

### Running analysis.py:

1. **Install Required Libraries**: Ensure that all necessary Python libraries and dependencies (such as pandas, textblob, nltk, etc.) are installed on your system.

2. **Open Terminal/Command Prompt**: Launch your terminal or command prompt.

3. **Navigate to File Directory**: Use the `cd` command to navigate to the directory where the `analysis.py` file is located.

4. **Execute Script**: Run the script by entering the following command:
   ```
   python analysis.py
   ```

5. **Wait for Completion**: Allow the script to run and complete the analysis process. Make sure that any required data files, such as input data or text files, are available in the specified directories as indicated within the script.

Following these instructions will help you to successfully execute the `extraction.py` and `analysis.py` scripts and perform the desired data extraction and analysis tasks.
