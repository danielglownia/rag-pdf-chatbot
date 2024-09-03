# rag-pdf-chatbot
Reading those explanation of benefits documents can be hard! This repo has a RAG (retrieval augmented generation) streamlit chatbot that does the hard work for you.

### Link to app 
https://eob-chatbot.streamlit.app/

### LLM Evaluation 

#### What is the best chunk size for our corpus of PDFs?
<img width="684" alt="Screenshot 2024-09-02 at 8 11 42 PM" src="https://github.com/user-attachments/assets/7eb20102-1c78-42a0-ac6a-2e2796cfe813">

#### Best performing embeddings for our corpus?  
<img width="688" alt="Screenshot 2024-09-02 at 8 11 29 PM" src="https://github.com/user-attachments/assets/9d6e4846-29d0-42bb-b2a8-57b35bbccdcd">

#### What is the best performing LLM?
<img width="641" alt="Screenshot 2024-09-02 at 8 11 16 PM" src="https://github.com/user-attachments/assets/5fd4e04f-ad82-48f0-85a3-67bc800e4fee">

#### Which approach has the best performance? (RAG vs RAG + LLM vs RAG + Fine-tune LLM)
<img width="853" alt="Screenshot 2024-09-02 at 8 11 02 PM" src="https://github.com/user-attachments/assets/29bfc50f-293f-45ef-98fd-c5110af0e788">

### Metrics Explained

BLEU Score - Assess response quality by comparing chatbot outputs to human references.

<img width="333" alt="image" src="https://github.com/user-attachments/assets/9c52afba-8f14-497a-84a4-c34764f5e972">

BLEU Score of 50+: Indicates a high level of understanding and ability for our chatbot.
Reflects the chatbot's capability to generate relevant and detailed responses.


### Architecture Diagram

<img width="924" alt="Screenshot 2024-09-02 at 6 26 17 PM" src="https://github.com/user-attachments/assets/f4b61384-f8b4-4369-9519-bd29bfc80555">

<img width="929" alt="Screenshot 2024-09-02 at 6 26 28 PM" src="https://github.com/user-attachments/assets/eea20088-cb70-40d2-a04b-4e8ef63fade0">


