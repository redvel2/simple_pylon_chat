<%inherit file="/cmain.mako" />
<div id="col-2">
<div style="text-align:center;"><form method="post" name="myform" action="/chats/search"><input type="text" name="query"/><input type="submit" name="search" value="Search"></div>
<div class="results">
%if c.search!={}:
<ul>
% for i in c.search['results']:
<li><a href="/chanel/${i.name}">#${i.name}</a></li>
%endfor
</ul>
%endif
</div>