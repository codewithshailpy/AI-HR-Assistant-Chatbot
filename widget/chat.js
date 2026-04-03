function toggleChat() {
    const chat = document.getElementById("chat-container");

    if (chat.classList.contains("hidden")) {
        chat.classList.remove("hidden"); // OPEN
    } else {
        chat.classList.add("hidden"); // CLOSE
    }
}

async function sendMessage() {

    const input = document.getElementById("user-input");
    const chatBox = document.getElementById("chat-box");
    const typing = document.getElementById("typing");

    const userMessage = input.value.trim();
    if (!userMessage) return;

    // Add user message
    chatBox.innerHTML += `<div class="message user">${userMessage}</div>`;
    input.value = "";

    chatBox.scrollTop = chatBox.scrollHeight;

    // Show typing
    typing.classList.remove("hidden");

    try {
        const response = await fetch("http://127.0.0.1:8000/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                question: userMessage
            })
        });

        const data = await response.json();

        // Hide typing
        typing.classList.add("hidden");

        // Add bot response
        chatBox.innerHTML += `<div class="message bot">${data.answer}</div>`;

    } catch (error) {
        typing.classList.add("hidden");
        chatBox.innerHTML += `<div class="message bot">Error connecting to server</div>`;
    }

    chatBox.scrollTop = chatBox.scrollHeight;
}