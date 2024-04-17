var chatData = {
    Sharvari: [
      { sender: 'Sharvari', message: "Hey What's today update!", dp: '../static/images/photu.jpg' },
      { sender: 'You', message: 'Designing is complete', dp: '../static/images/renuka.jpg' },
    ],
    Siddhi: [
      { sender: 'Siddhi', message: 'Do you call her today?', dp: '../static/images/pic.jpg' },
      { sender: 'You', message: 'Nope', dp: '../static/images/your_dp.jpg' },
    ],
    xyz: [
      { sender: 'xyz', message: 'Hi there!', dp: 'xyz_dp.jpg' },
      { sender: 'You', message: 'Hello! How are you?', dp: '../images/your_dp.jpg' },
    ],
    contact4: [
      { sender: 'abc', message: 'Hey thanks for reminding', dp: 'abc_dp.jpg' },
      { sender: 'You', message: 'Np', dp: '../images/your_dp.jpg' },
    ],
    contact5: [
      { sender: 'lmn', message: 'Hi there!', dp: 'lmn_dp.jpg' },
      { sender: 'You', message: 'Hello! How are you?', dp: '../images/your_dp.jpg' },
    ],
  };

  function showChat(contact) {
var chatContainer = document.getElementById('chat-container');
var messages = chatData[contact];
var chatHtml = '<h2>' + contact + '</h2>';

if (messages) {
  messages.forEach(function (msg) {
    var messageClass = msg.sender === 'You' ? 'user-message' : 'contact-message';
    chatHtml += '<div class="message-container"><p class="message ' + messageClass + '"><img src="' + msg.dp + '" alt="DP"><strong>' + msg.sender + ':</strong> ' + msg.message + '</p></div>';
  });

  chatContainer.innerHTML = chatHtml;

  // Scroll to the bottom of the chat container
  chatContainer.scrollTop = chatContainer.scrollHeight;
} else {
  chatHtml += '<p>No messages available for ' + contact + '</p>';
  chatContainer.innerHTML = chatHtml;
}
}

  function sendMessage() {
      var inputElement = document.querySelector('#message-input input');
      var message = inputElement.value;

  // For demonstration purposes, let's assume the contact is always 'Sharvari'
  var contact = 'Sharvari';
  var chatContainer = document.getElementById('chat-container');

  if (message) {
    var dp = '../static/images/your_dp.jpg'; // Use the same DP for "You" messages
    var messageHtml = '<div class="message-container"><p class="message user-message"><img src="' + dp + '" alt="Your DP"><strong>You:</strong> ' + message + '</p></div>';
    chatContainer.innerHTML += messageHtml;
    inputElement.value = ''; // Clear the input after sending
  }
}