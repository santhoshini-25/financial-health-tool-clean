import requests
import os

# Hugging Face API details (free tier) - Using distilgpt2 for reliable free access
API_URL = "https://api-inference.huggingface.co/models/distilgpt2"
HEADERS = {"Authorization": f"Bearer {os.getenv('HUGGINGFACE_API_KEY')}"}

def analyze_financial_health(data_dict, industry):
    # data_dict is a dict like {'revenue': 1000, 'expenses': 500}
    prompt = f"""
    Analyze the following financial data for an {industry} SME:
    Revenue: {data_dict.get('revenue', 0)}
    Expenses: {data_dict.get('expenses', 0)}
    Provide a creditworthiness score (1-10), risks, optimization suggestions, and product recommendations.
    """
    
    try:
        # Call Hugging Face API
        response = requests.post(API_URL, headers=HEADERS, json={"inputs": prompt, "parameters": {"max_length": 150, "temperature": 0.7}})
        response.raise_for_status()  # Raise error for bad responses
        
        # Parse the response (Hugging Face returns a list of dicts)
        result = response.json()
        if isinstance(result, list) and result:
            generated_text = result[0].get("generated_text", "No insights generated.")
            # Clean up: Remove the prompt from the response if repeated
            insights = generated_text.replace(prompt, "").strip()
            return insights or "AI insights: Based on data, maintain good financial practices."
        else:
            return "Error: Unexpected response format from AI."
    except requests.exceptions.RequestException as e:
        # If API fails (e.g., 410, network issues), fall back to mock insights
        print(f"API Error: {e}. Using mock insights.")  # For debugging
        return generate_mock_insights(data_dict, industry)
    except Exception as e:
        return f"Unexpected error: {str(e)}. Using mock insights." + generate_mock_insights(data_dict, industry)

def generate_mock_insights(data_dict, industry):
    # Free, local mock function as a fallback
    revenue = data_dict.get('revenue', 0)
    expenses = data_dict.get('expenses', 0)
    score = 5  # Default
    if revenue > expenses * 1.5:
        score = 8
    elif revenue < expenses:
        score = 3
    
    return f"Mock AI Insights for {industry} SME: Creditworthiness score: {score}/10. Risks: Potential cash flow issues if expenses exceed revenue. Suggestions: Optimize expenses and explore cost-saving products. Recommendations: Consider low-interest loans from NBFCs."