# ReCallForge v1

![Python](https://img.shields.io/badge/Python-3.14-blue)
![PySide6](https://img.shields.io/badge/PySide6-6.11-green)
![Groq-Powered](https://img.shields.io/badge/AI-Groq-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

ReCallForge is a desktop application designed to help learners study more effectively using **active recall**, one of the most powerful learning techniques supported by scientific research.

Instead of passively rereading notes, ReCallForge allows you to store information and then interact with an AI that asks you questions about what you've learned. This transforms studying into an active process, helping you strengthen your memory and improve long-term retention.

Built with **Python**, **PySide6**, and the **Groq API**, ReCallForge aims to make evidence-based learning simple and accessible.

---

## Why ReCallForge?

If you're a student, language learner, programmer, or simply someone trying to remember information more effectively, ReCallForge may be useful for you.

Research consistently shows that **retrieving information from memory** is far more effective than repeatedly rereading material. This technique is known as **active recall** or **retrieval practice**.

ReCallForge was built around this idea: helping learners turn their own notes into an interactive study experience powered by AI.

---

## Features

* 🧠 Store your study information quickly and easily.
* 🤖 Practice using AI-generated active recall questions.
* ✍️ Answer open-ended questions.
* 📝 Fill in the blanks to strengthen memory.
* ✅ Practice with multiple-choice questions.
* 💾 Local storage of your information.
* 🖥️ Simple and beginner-friendly desktop interface.

---

## Scientific Background

Active recall is one of the most researched learning techniques in educational psychology.

Some of the studies supporting retrieval practice include:

* **Abbott (1909):** One of the earliest studies demonstrating the benefits of retrieval over repeated exposure.
* **Gates (1917):** Found that students who actively recited information significantly outperformed those who only reread material.
* **Spitzer (1939):** Showed that testing can reduce forgetting and strengthen retention.
* **Tulving (1967):** Demonstrated that retrieval itself strengthens memory traces.
* **Karpicke & Roediger (2006):** Established the famous "testing effect," showing that retrieval practice leads to superior long-term learning.
* **Karpicke & Roediger (2008):** Found that repeated testing dramatically improves retention.
* **McDaniel (2011):** Demonstrated successful classroom integration of retrieval practice.
* **Dunlosky et al. (2013):** Identified active recall and spaced repetition as two of the highest-utility study techniques.
* **Recent reviews (2024):** Continue to associate active recall with improved academic performance and confidence.

The science is clear: testing yourself is not just a way to measure learning—it is a powerful way to create learning.

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Adamdev-AI/ReCall.git
cd ReCall
```

### 2. Create a Groq API key

Visit:

https://console.groq.com/keys

Create a free API key.

### 3. Configure your API key

Open the `api.env` file and replace:

```env
GROQ=your_api_key_here
```

with your own API key.

### 4. Run the application

```bash
python main.py
```

---

## How It Works

When ReCallForge starts, it automatically creates a text file named:

```text
ReCallForge informations.txt
```

This file stores all of the information you add through the application.

The AI reads this stored information and uses it to generate personalized recall questions based on your own notes.

> **Note:** The current version depends on this exact filename, so it should not be renamed.

---

## How to Use ReCallForge

### Step 1: Add Information

Click the **Add** button in the navigation bar.

Insert the information you want to remember and press **Add**.

Your information will automatically be saved.

<img width="1366" height="768" alt="Screenshot (188)" src="https://github.com/user-attachments/assets/c105c68e-2144-4cb7-99c5-46bbf055fee6" />

---

### Step 2: Study With AI

Go back to the Home page and start chatting with the AI.

The AI will use your stored information to generate questions and help you practice active recall.

<img width="1366" height="768" alt="Screenshot (189)" src="https://github.com/user-attachments/assets/2fa04d0d-b372-4d03-82e9-b815ded1a39b" />

That's it—simple and effective.

---

## Technologies Used

* Python
* PySide6
* Groq API

---

## What I Learned

ReCallForge is my first major software project, and building it taught me a lot.

During this project, I learned:

* How to structure a real application.
* How to build desktop interfaces using PySide6.
* How to connect different components together.
* How to work with files and local storage.
* How to integrate AI APIs into an application.
* How to handle user interactions and application logic.
* How much debugging is actually part of programming!

This project represents a major milestone in my journey as a developer.

---

## Roadmap (V2)

Planned improvements for the next version include:

* 🔍 Google Search integration to enrich explanations.
* ⚙️ Add settings and customization options.
* 💬 Support for multiple chats.
* ✏️ Edit stored information directly from the application.
* 🧠 Smarter and more diverse AI-generated questions.
* 📚 Better organization of study materials.

---

## Contributing

Suggestions, feedback, and contributions are always welcome.

If you have ideas for improving ReCallForge, feel free to open an issue or submit a pull request.

---

## License

This project is released under the MIT License.

---

Thank you for checking out ReCallForge.

If this project helps you study more effectively, consider giving it a ⭐ on GitHub!
