# Food Nutrition Analyzer
The Food Macro and Micro Nutrition Analyzer is an intelligent digital tool designed to break down the exact nutritional profile of any meal, ingredient, or recipe based on user-inputted quantities. By processing natural language or structured data, the system instantly calculates both macro and micronutrients to give users complete transparency over what they consume.

## Prerequisites
- Python 3.11 or higher
- Anthropic API key
## Installation

### Backend Setup
1. Navigate to the root directory:
```bash
cd food-nutri
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

4. Set up your OpenAI API key:
```bash
export ANTHROPIC_API_KEY='your-api-key-here'  # On Windows, use: set ANTHROPIC_API_KEY=your-api-key-here
```


5. Run the Project:
```bash
python main.py
```

## License
Please refer the LICENSE file.