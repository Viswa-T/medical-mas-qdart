# Medical Record Retrieval Assistant (MAS – Qdrant)

## Problem (Real-World Context)

In modern healthcare systems, hospitals store large volumes of patient data collected over multiple visits and years. While existing Electronic Health Record (EHR) systems can retrieve patient information using identifiers such as patient ID or mobile number, they struggle when retrieval is needed based on clinical context or situation.

Doctors frequently encounter cases where patient symptoms are vague or overlapping, medical notes are written differently by different doctors, exact keywords are unknown or unavailable, and subtle similarities with past cases are difficult to recall.

Traditional keyword-based search and structured database queries fail to capture semantic meaning, forcing doctors to rely heavily on personal memory and intuition. This increases cognitive load and can lead to important historical context being overlooked.

---

## Proposed Solution

This project implements a Medical Record Retrieval Assistant that acts as a semantic memory layer for medical records.

Instead of retrieving data by patient identity, the system retrieves records based on contextual similarity. Medical records are converted into vector embeddings and stored in Qdrant, enabling natural language queries that retrieve historically similar cases.

The system helps medical professionals retrieve relevant past patient cases by situation, explore semantically similar medical contexts, and reduce reliance on manual memory recall.

This system does not diagnose diseases or predict outcomes. It is designed strictly as a decision-support and contextual awareness tool.

---

## Why This Is Different From Existing Systems

Traditional hospital systems rely on identity-based lookup and keyword matching. This project enables context-based retrieval using semantic understanding and natural language queries. It augments human memory by enabling case similarity exploration rather than replacing existing hospital databases.

---

## System Architecture

User Query  
→ Sentence Transformer (Embedding Model)  
→ Qdrant Vector Database (Semantic Memory)  
→ Contextually Relevant Medical Records

---

## Technologies Used

Python  
Qdrant (Vector Database)  
Sentence Transformers (Embeddings)

---

## How to Run

Step 1: Install dependencies  
pip install -r requirements.txt

Step 2: Ingest patient medical records  
python ingest.py

Step 3: Run the retrieval assistant  
python main.py

Step 4: Enter a medical condition or context (for example: asthma, chronic kidney disease) to retrieve relevant patient histories.

---

## Ethical Considerations & Limitations

The system does not provide medical diagnosis or treatment recommendations. All patient records used are synthetic and anonymized. The tool is intended to support clinical reasoning, not replace medical professionals.

---

## Conclusion

This project demonstrates how semantic retrieval and long-term memory systems can enhance medical decision-making by providing fast, context-aware access to historical cases. By reducing reliance on keyword searches and human memory alone, the system improves clinical context awareness while maintaining ethical responsibility.
