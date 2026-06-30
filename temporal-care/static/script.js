async function sendMessage() {
    const input = document.getElementById('user-input');
    const history = document.getElementById('chat-history');
    const message = input.value;
    
    if (!message) return;
    
    history.innerHTML += `<p><b>You:</b> ${message}</p>`;
    input.value = '';
    
    const response = await fetch('/chat', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({message})
    });
    
    const data = await response.json();
    history.innerHTML += `<p><b>Temporal Care:</b> ${data.response}</p>`;
}
