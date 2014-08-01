<%inherit file="/cmain.mako" />
<script type="text/javascript">
    $(document).ready(function(){
       $('#add_message').ajaxForm(function() {
         $('#to_user').val('');
         $('#message_body').val('');
});
        intId=setInterval(interval, 5*1000);
});
function add_to(name) {
	  $('#to_user').val(name);
}

function interval() {
        var intr = 5;
        var ul=$('ul#messages');
        var timestamp = $('ul#messages li:last').attr('timestamp');
        var url = 'display_messages/'+timestamp;
        var  html='Users online: ';
        $.getJSON(url, {}, function(json, scroll) {
            ul.html(ul.html()+json.messages);
            if (json.messages) {
               var height=$("#messages_area").height(); 
               $("#messages_area").animate({'scrollTop':height}, 'slow');
            }
            for (i in json.users) {
               html+=json.users[i]+','
            };
            $('#online_users').html(html);
            html='Users online: ';
	});
};
</script>
<div id="col-2">
<div id="chat_body">
<h1>Welcome to chanel:<b>${c.title}</b></h1>
<div id="online_users" style="text-align:center;">Loading..</div>
<div id="messages_area">
<ul id="messages">
<li timestamp=${c.timestamp} style="display:none;"></li>
</ul></div>
%if c.user!={}:
<div id="input_area"><form method="post" action="/chats/add_message" id="add_message"><input type="hidden" name="chanel" value="${c.chanel}"><label>To:</label><input type="text" id="to_user" name="to"><br/><textarea name="body" id="message_body"></textarea><input type="submit" value="Send" id="send_message"></form></div>
%else:
<div id="input_area"><a href="/auth/signin">Sign in</a> to write a message</div>
%endif
</div></div>