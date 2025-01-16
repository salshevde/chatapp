const chatSlug = document.getElementById('chat-navbar').getAttribute('data-chat-slug');
const username = document.getElementById('chat-navbar').getAttribute('data-username');

const chatSocket = new WebSocket(
    'ws://' + window.location.host + '/ws/chat/'+chatSlug+'/'
);

const messagesContainer = document.getElementById('messages-container')
const chatInput = document.getElementById('chat-text-input')
const sendButton = document.getElementById('send-chat-btn')

chatSocket.onmessage = function(e){
    const data = JSON.parse(e.data)

    const messageDiv = document.createElement('div')

    messageDiv.className = data.username === username ? 'user-message': 'message';

    messageDiv.innerHTML = `
            <strong>${data.username}:</strong>
            <p>${data.message}</p>
            <small>${new Date(data.timestamp).toLocaleString()}</small>
    `
    messagesContainer.appendChild(messageDiv)
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
};

chatSocket.onclose = function(e){
    console.error('Chat socket closed unexpectedly');
}

function sendMessage(){
    const message = chatInput.value.trim();
    if(message){
        chatSocket.send(JSON.stringify({
            'message': message
        }));

        chatInput.value = '';
    }
}

sendButton.addEventListener('click', sendMessage);
chatInput.addEventListener('keypress', function(e){
    if(e.key === 'Enter'){
        sendMessage();
    }
})

window.onload = function(){
    messagesContainer.scrollTop = messagesContainer.scrollHeight
}
