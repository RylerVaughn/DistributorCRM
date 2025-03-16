
"use strict";

// load in the clients from the context into the script
const conversations = JSON.parse(document.getElementById("conversation-data").textContent);
const contactButtons = Array.from(document.getElementsByClassName("contact-button"));
const messageArea = document.getElementById("message-tab");

contactButtons.forEach(contactButton => {

    contactButton.addEventListener("click", function() {

        messageArea.replaceChildren();

        if (conversations.hasOwnProperty(contactButton.textContent.trim()) && !conversations[contactButton.textContent.trim()].length == 0) {
            for (let message of conversations[contactButton.textContent.trim()]) {

                let messageBody = document.createElement("p");
                messageBody.textContent = message['body'];
                messageBody.setAttribute("class", "message-body");
    
                let textMessage = document.createElement("div");
                
                if (message["sender"] == "+18127821348") {
                    textMessage.setAttribute("class", "outbound-message");
                } else {
                    textMessage.setAttribute("class", "inbound-message");
                }
    
                textMessage.appendChild(messageBody);
    
                messageArea.appendChild(textMessage);
            }
        } else {

            let noMessagesHeading = document.createElement("h1");
            noMessagesHeading.textContent = `No messages found with ${contactButton.textContent.trim()}.`;
            noMessagesHeading.setAttribute("class", "no-messages-found");

            messageArea.appendChild(noMessagesHeading);
        }
    });
});