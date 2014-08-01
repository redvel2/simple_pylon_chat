% for b in c.messages:
<li timestamp=${b.timestamp} class="message"><a href="#" onclick=add_to(name) class="chat_user" name="${b.person_name}">${b.person_name}:</a></b>
% if b.to != '':
>> <b><a href="#" onclick=add_to(name) class="chat_user" name="${b.to}">${b.to}:</a></b>
% endif
<span class="m_date">${b.date.split(' ')[1]}</span>
<br/>
${b.body}
</li>
% endfor