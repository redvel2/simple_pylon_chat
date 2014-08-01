<%inherit file="/base_user.mako" />

<%def name="head_tags()">
  <title>${c.title}</title>
   <script src="http://code.jquery.com/jquery-1.11.0.min.js"></script>
   <script src="http://malsup.github.io/jquery.form.js"></script>
   <script src="/jquery.tinyscrollbar.js"></script>
   <link rel="stylesheet" href="/chat.css">
</%def>

<%def name="user_panel()"><div id="col-1">
% if c.user!={}:
<div id="userpan">Hello, <b>${c.user['name']}</b> <a href="/auth/logout">[exit]</a><br/>
Chanels: <a href="/chats/search">[search]</a>
<div id="form_create">
${h.form('/chats/create_chat', method='post')}
${h.text('chat_name')}
${h.submit('button', 'Create')}
${h.end_form()}
</div>
<h2>Your chanels:</h2>
<ul>
<li><a href="/chanel/main">#Main</a></li>
% for a in c.user['chanels']:
<li><a href="/chanel/${a.name}">&nbsp#${a.name}</a></li>
% endfor
</ul>
</div>
%else:
<div id="userpan"><a href="/auth/signin">Sign in</a> to join a chat</div>
% endif
</div>
</%def>
<div id="col-2"></div>