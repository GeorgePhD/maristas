const inputField = document.querySelector('#userInput');
let messageCount = 0;  // Counter to track the number of messages

const sendMessage = () => {
    const userInput = inputField.value;

    if (userInput.trim() == '') return;

    const chatbox = document.querySelector('#chatbox');
    
    // Increment the message count
    messageCount++;

    // Smooth transition when the chat exceeds 10 messages
    if (messageCount > 5) {
        // Apply fade-out class to the chatbox
        chatbox.classList.add('fade-out');

        setTimeout(() => {
            // Clear the chatbox after fade-out is complete
            chatbox.innerHTML = '<h3>...</h3>';  // Clear the chatbox
            messageCount = 1;  // Reset the counter
            
            // Remove fade-out and add fade-in class
            chatbox.classList.remove('fade-out');
            chatbox.classList.add('fade-in');
            
            // Remove fade-in class after the transition
            setTimeout(() => {
                chatbox.classList.remove('fade-in');
            }, 500);  // Duration of the fade-in effect
        }, 500);  // Duration of the fade-out effect
    }

    // Add the user's message to the chatbox
    const userMessage = `<p><strong>You:</strong> ${userInput}</p>`;
    chatbox.innerHTML += userMessage;

    fetch('/get_response', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: userInput }),
    })
    .then(response => response.json())
    .then(data => {
        // Add the bot's response to the chatbox
        const botMessage = `<p><strong>Bot:</strong> ${data.response}</p>`;
        chatbox.innerHTML += botMessage;
        
        // Clear input field
        inputField.value = '';
    })
    .catch(error => console.error('Error:', error));
}

// Listen for 'Enter' key to send the message
inputField.addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        sendMessage();
    }
});
