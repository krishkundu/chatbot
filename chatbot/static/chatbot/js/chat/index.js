var element = $('.floating-chat');
var myStorage = localStorage;

if (!myStorage.getItem('chatID')) {
    myStorage.setItem('chatID', createUUID());
}

setTimeout(function() {
    element.addClass('enter');
}, 1000);

element.click(openElement);

function openElement() {
    var messages = element.find('.messages');
    var textInput = element.find('.text-box');
    element.find('>i').hide();
    element.addClass('expand');
    element.find('.chat').addClass('enter');
    var strLength = textInput.val().length * 2;
    textInput.keydown(onMetaAndEnter).prop("disabled", false).focus();
    element.off('click', openElement);
    element.find('.header button').click(closeElement);
    element.find('#sendMessage').click(sendNewMessage);
    messages.scrollTop(messages.prop("scrollHeight"));
}

function closeElement() {
    element.find('.chat').removeClass('enter').hide();
    element.find('>i').show();
    element.removeClass('expand');
    element.find('.header button').off('click', closeElement);
    element.find('#sendMessage').off('click', sendNewMessage);
    element.find('.text-box').off('keydown', onMetaAndEnter).prop("disabled", true).blur();
    setTimeout(function() {
        element.find('.chat').removeClass('enter').show()
        element.click(openElement);
    }, 500);
}

function createUUID() {
    // http://www.ietf.org/rfc/rfc4122.txt
    var s = [];
    var hexDigits = "0123456789abcdef";
    for (var i = 0; i < 36; i++) {
        s[i] = hexDigits.substr(Math.floor(Math.random() * 0x10), 1);
    }
    s[14] = "4"; // bits 12-15 of the time_hi_and_version field to 0010
    s[19] = hexDigits.substr((s[19] & 0x3) | 0x8, 1); // bits 6-7 of the clock_seq_hi_and_reserved to 01
    s[8] = s[13] = s[18] = s[23] = "-";

    var uuid = s.join("");
    return uuid;
}

/*function sendNewMessage() {
    var userInput = $('.text-box');
    var newMessage = userInput.html().replace(/\<div\>|\<br.*?\>/ig, '\n').replace(/\<\/div\>/g, '').trim().replace(/\n/g, '<br>');

    if (!newMessage) return;

    var messagesContainer = $('.messages');

    messagesContainer.append([
        '<li class="self">',
        newMessage,
        '</li>'
    ].join(''));

    // clean out old message
    userInput.html('');
    // focus on input
    userInput.focus();

    messagesContainer.finish().animate({
        scrollTop: messagesContainer.prop("scrollHeight")
    }, 250);
}*/

function fire_ajax_submit_chat(chatText) {
    
    var chatMsg = {}
    chatMsg["req_msg"] = chatText;
    chatMsg["res_msg"] = '';
    
    $.ajax({
        type: "POST",
        contentType: "application/json",
        url: "/chat-api/post",
        csrfmiddlewaretoken: "{{ csrf_token }}",
        data: JSON.stringify(chatMsg),
        dataType: 'json',
        cache: false,
        timeout: 600000,
        success: function (data) {
        	console.log("SUCCESS : ", data.result);
            console.log("SUCCESS : ", data.response);
            //insertChat('you',data.response,d.getTime());
            var userInput = $('.text-box');
            var messagesContainer = $('.messages');
            
            var resp_arr = JSON.parse(data.response);
            
            
            for(b in resp_arr){
            	
            	console.log(">>>>>>>>111"+resp_arr[b].recipient_id);
            	console.log(">>>>>>>>111"+resp_arr[b].text);
            }
            //delay_bot_response();
            //setTimeout(display_response(resp_arr),5000);
        	//bot response
        	
        	for(a in resp_arr){
        		var txt = resp_arr[a].text;
        		console.log(">>>>>>>>Text1 "+txt);
        		console.log(">>>>>>>>a "+a);
        		if(a == 0){
        			console.log(">>>>>>>>a==0");
        			//display_response(txt);
        			console.log(">>>>>>>>display response");
        			doSetTimeout(txt, a+1)
   			
        		} else {
        			console.log(">>>>>>>>a!=0");
        			doSetTimeout(txt, a+2)
        			console.log(">>>>>>>>a!=0 delay"+txt);
        			
        		}
        	}
        	//delete_delay()
          	
            
            // clean out old message
            userInput.html('');
            // focus on input
            userInput.focus();

            messagesContainer.finish().animate({
                scrollTop: messagesContainer.prop("scrollHeight")
            }, 250);
        },
        error: function (e) {
            alert("Please check username and password and try again.");
        }
    });
}

function doSetTimeout(i,j) {
	  delay_bot_response();
	  setTimeout(function() { 
		  display_response(i);
			delete_delay();

	  }, 2000*j);
}

function delete_delay(){
	$("#rmv_li").remove();
}

function delayed_resp(txt){
	delay_bot_response();
	setTimeout(display_response(txt),4000);
}

function display_response(resp) {
	var messagesContainer = $('.messages');
	console.log("display_response "+resp);
	messagesContainer.append([
        '<li class="other">',
        resp,
        '</li>'
    ].join(''));
}

function delay_bot_response(){
	
	
	var messagesContainer = $('.messages');
		messagesContainer.append([
        '<li class="other" id="rmv_li">',
        '<div class="spinner"><div class="bounce1"></div><div class="bounce2"></div><div class="bounce3"></div></div>',
        '</li>'
    ].join(''));
}


function sendNewMessage() {

    //update the ui and call the ajax method
    var userInput = $('.text-box');
    var newMessage = userInput.html().replace(/\<div\>|\<br.*?\>/ig, '\n').replace(/\<\/div\>/g, '').trim().replace(/\n/g, '<br>');

    if (!newMessage) return;

    var messagesContainer = $('.messages');

    messagesContainer.append([
        '<li class="self">',
        newMessage,
        '</li>'
    ].join(''));

    // clean out old message
    userInput.html('');
    // focus on input
    userInput.focus();

    messagesContainer.finish().animate({
        scrollTop: messagesContainer.prop("scrollHeight")
    }, 250);
    //call the ajax submit method
    fire_ajax_submit_chat(newMessage);
}







function onMetaAndEnter(event) {
    if ((event.metaKey || event.ctrlKey) && event.keyCode == 13) {
        sendNewMessage();
    }
}