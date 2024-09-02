# rag-pdf-chatbot
Reading those explanation of benefits documents can be hard! This repo has a RAG (retrieval augmented generation) streamlit chatbot that does that hard work for you.

### Link to app 
https://eob-chatbot.streamlit.app/

### LLM Evaluation 

| Insurance Document  | BLEU Score |
| ------------- | ------------- |
| Aetna  | 54.23  |
| BCBS  | 59.84  |
| UHC  | 55.62  |

BLEU Score - Assess response quality by comparing chatbot outputs to human references.

<img width="333" alt="image" src="https://github.com/user-attachments/assets/9c52afba-8f14-497a-84a4-c34764f5e972">

BLEU Score of 50+: Indicates a high level of understanding and ability for our chatbot.
Reflects the chatbot's capability to generate relevant and detailed responses.


### Architecture Diagram

<img width="924" alt="Screenshot 2024-09-02 at 6 26 17 PM" src="https://github.com/user-attachments/assets/f4b61384-f8b4-4369-9519-bd29bfc80555">

<img width="929" alt="Screenshot 2024-09-02 at 6 26 28 PM" src="https://github.com/user-attachments/assets/eea20088-cb70-40d2-a04b-4e8ef63fade0">


