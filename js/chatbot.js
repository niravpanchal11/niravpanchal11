// Chatbot functionality
class Chatbot {
    constructor() {
        this.isOpen = false;
        this.chatHistory = [];
        this.apiUrl = "http://localhost:8000/chat";
        this.init();
    }

    init() {
        // Create chatbot UI
        this.createChatbotUI();
        this.attachEventListeners();
    }

    createChatbotUI() {
        // Check if chatbot already exists
        if (document.getElementById("chatbot-widget")) return;

        // Create chatbot widget HTML
        const chatbotHTML = `
            <div id="chatbot-widget" class="chatbot-widget">
                <!-- Chatbot Button -->
                <button id="chatbot-toggle" class="chatbot-toggle" aria-label="Open chatbot">
                    <i class="bi bi-chat-dots-fill"></i>
                </button>

                <!-- Chatbot Container -->
                <div id="chatbot-container" class="chatbot-container">
                    <!-- Header -->
                    <div class="chatbot-header">
                        <div class="chatbot-header-content">
                            <h3>Nirav's Assistant</h3>
                            <p>Ask me anything! 🤖</p>
                        </div>
                        <button id="chatbot-close" class="chatbot-close-btn" aria-label="Close chatbot">
                            <i class="bi bi-x-lg"></i>
                        </button>
                    </div>

                    <!-- Chat Messages -->
                    <div id="chatbot-messages" class="chatbot-messages">
                        <div class="chatbot-message bot-message">
                            <p>Hi! 👋 I'm Nirav's AI Assistant. Ask me anything about Nirav's skills, experience, or how to contact him!</p>
                        </div>
                    </div>

                    <!-- Input Area -->
                    <div class="chatbot-input-area">
                        <input 
                            type="text" 
                            id="chatbot-input" 
                            class="chatbot-input" 
                            placeholder="Type your message..."
                            autocomplete="off"
                        >
                        <button id="chatbot-send" class="chatbot-send-btn" aria-label="Send message">
                            <i class="bi bi-send-fill"></i>
                        </button>
                    </div>
                </div>
            </div>
        `;

        // Add chatbot to body
        document.body.insertAdjacentHTML("beforeend", chatbotHTML);
    }

    attachEventListeners() {
        const toggleBtn = document.getElementById("chatbot-toggle");
        const closeBtn = document.getElementById("chatbot-close");
        const sendBtn = document.getElementById("chatbot-send");
        const input = document.getElementById("chatbot-input");

        toggleBtn.addEventListener("click", () => this.toggleChatbot());
        closeBtn.addEventListener("click", () => this.toggleChatbot());
        sendBtn.addEventListener("click", () => this.sendMessage());
        input.addEventListener("keypress", (e) => {
            if (e.key === "Enter") this.sendMessage();
        });
    }

    toggleChatbot() {
        const container = document.getElementById("chatbot-container");
        this.isOpen = !this.isOpen;
        container.classList.toggle("open", this.isOpen);
    }

    async sendMessage() {
        const input = document.getElementById("chatbot-input");
        const message = input.value.trim();

        if (!message) return;

        // Add user message to chat
        this.addMessageToChat(message, "user");
        input.value = "";

        // Show typing indicator
        this.showTypingIndicator();

        try {
            // Send message to backend
            const response = await fetch(this.apiUrl, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ message: message }),
            });

            if (!response.ok) throw new Error("Network response was not ok");

            const data = await response.json();
            
            // Remove typing indicator and add bot response
            this.removeTypingIndicator();
            this.addMessageToChat(data.response, "bot");
        } catch (error) {
            console.error("Error:", error);
            this.removeTypingIndicator();
            this.addMessageToChat(
                "Sorry, I'm having trouble connecting to my backend. Please try again later or contact me directly at niravpanchal9980@gmail.com 😊",
                "bot"
            );
        }
    }

    addMessageToChat(message, sender) {
        const messagesContainer = document.getElementById("chatbot-messages");
        const messageElement = document.createElement("div");
        messageElement.className = `chatbot-message ${sender}-message`;
        
        const messageText = document.createElement("p");
        messageText.textContent = message;
        messageElement.appendChild(messageText);
        
        messagesContainer.appendChild(messageElement);
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
    }

    showTypingIndicator() {
        const messagesContainer = document.getElementById("chatbot-messages");
        const typingElement = document.createElement("div");
        typingElement.className = "chatbot-message bot-message typing-indicator";
        typingElement.id = "typing-indicator";
        typingElement.innerHTML = '<span></span><span></span><span></span>';
        
        messagesContainer.appendChild(typingElement);
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
    }

    removeTypingIndicator() {
        const typingElement = document.getElementById("typing-indicator");
        if (typingElement) typingElement.remove();
    }
}

// Initialize chatbot when DOM is ready
document.addEventListener("DOMContentLoaded", () => {
    new Chatbot();
});
