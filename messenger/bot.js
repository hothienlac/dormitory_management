const request = require('request');

const PAGE_ACCESS_TOKEN = 'EAAHyyBgow1IBAPmG3yD3dWtMFnJZBQlGbbZCehTS5iXeiWabzlUbYrqaNzR6Nzw0INQi4BZAN51JREuFltiSNaXLklhnmsHGduw967UzTj3IH6rH9JinO1BZCRTtEPPnvQIUsx6ERAcS8b7rzFPEya9P94i1wOFajlZAiZCk5rFJPUS7YY4PmTOLnu4HHr81UZD';


class Bot {

    constructor(server) {
        this.server = server;
    }

    handleMessage(sender_psid, received_message) {
        this.server.receive(sender_psid, received_message.text)

        let response;
  
        // Checks if the message contains text
        if (received_message.text) {    
            // Create the payload for a basic text message, which
            // will be added to the body of our request to the Send API
            response = {
            "text": `You sent the message: "${received_message.text}". Now send me an attachment!`
            }
        } else if (received_message.attachments) {
            // Get the URL of the message attachment
            let attachment_url = received_message.attachments[0].payload.url;
            response = {
            "attachment": {
                "type": "template",
                "payload": {
                "template_type": "generic",
                "elements": [{
                    "title": "Is this the right picture?",
                    "subtitle": "Tap a button to answer.",
                    "image_url": attachment_url,
                    "buttons": [
                        {
                            "type": "postback",
                            "title": "Yes!",
                            "payload": "yes",
                        },
                        {
                            "type": "postback",
                            "title": "No!",
                            "payload": "no",
                        }
                    ],
                }]
                }
            }
            }
        } 
        
        // Send the response message
        Bot.callSendAPI(sender_psid, response);
    }

    handlePostback(sender_psid, received_postback) {
        console.log('ok')
        let response;
        // Get the payload for the postback
        let payload = received_postback.payload;
      
        // Set the response based on the postback payload
        if (payload === 'yes') {
            response = { "text": "Thanks!" }
        } else if (payload === 'no') {
            response = { "text": "Oops, try sending another image." }
        }
        // Send the message to acknowledge the postback
        Bot.callSendAPI(sender_psid, response);
    }

    handleReaction(sender_psid, received_reaction) {

    }




    static callSendAPI(sender_psid, response) {
        // Construct the message body
        let request_body = {
            "recipient": {
                "id": '3469845626365526'
            },
            "message": `${sender_psid}: ${response}`
        }
    
        // Send the HTTP request to the Messenger Platform
        request({
            "uri": "https://graph.facebook.com/v2.6/me/messages",
            "qs": { "access_token": PAGE_ACCESS_TOKEN },
            "method": "POST",
            "json": request_body
        }, (err, res, body) => {
        if (!err) {
            console.log('message sent!')
        } else {
            console.error("Unable to send message:" + err);
        }
        }); 
    }

}

module.exports = Bot