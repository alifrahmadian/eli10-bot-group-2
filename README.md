# Explain Like I'm 10 Chatbot - Kelompok 2
1. Apa itu LangChain?

LangChain adalah framework Python (dan JS) untuk membangun aplikasi berbasis LLM dengan cara yang terstruktur dan modular.

Intinya: LangChain membantu kamu menghubungkan LLM dengan data, tools, dan alur kerja (workflow).

Contoh tanpa LangChain:
response = llm("Apa itu AI?")
Dengan LangChain:
chain = PromptTemplate + LLM + OutputParser
result = chain.run("Apa itu AI?")

Jadi bukan cuma “tanya jawab”, tapi bisa:

Chatbot dengan memory
QA dari PDF / database
Agent (bisa pakai tools: search, calculator, dll)

2.Kenapa tidak langsung pakai API LLM saja?

Jawaban jujurnya:

Bisa. Bahkan harus ngerti dulu API-nya.tetapi, Kalau project mulai kompleks, kamu bakal ketemu masalah:

Tanpa LangChain:
Prompt berantakan
Sulit handle banyak step (multi-step reasoning)
Ribet integrasi ke database / file
Tidak ada struktur jelas
Dengan LangChain:Ada struktur “chain”,Bisa gabungkan,LLM,Prompt,Tools,Memory,Lebih scalable (cocok untuk project AI serius)

3. Apa itu LLM?

LLM (Large Language Model) adalah model AI yang dilatih dari teks dalam jumlah besar untuk:

menjawab pertanyaan
menulis teks
coding
reasoning
Contoh LLM:
GPT
Claude
LLaMA

Cara kerjanya memprediksi kata berikutnya berdasarkan konteks.

Apa itu Prompt?

Prompt adalah input yang kamu berikan ke LLM.

Contoh:
Jelaskan apa itu machine learning dengan bahasa sederhana

Kualitas output = kualitas prompt

Makanya ada istilah Prompt Engineering

Apa itu Chain?

Chain adalah rangkaian langkah (pipeline) yang menghubungkan beberapa komponen.

Contoh sederhana:
User Input → Prompt Template → LLM → Output
\
User → Ambil data DB → Format prompt → LLM → Validasi → Output

Jadi chain = workflow AI
