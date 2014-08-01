<%inherit file="/base.mako" />

<%def name="head_tags()">
  <link rel="stylesheet" href="/main.css">
</%def>

<div class="middle"><div class="middle_content"><h1>Sign in to your own account</h1>
${h.form('/auth/signin',method='post')}
<label>Email</label>
${h.text('email')}
<br/><label>Password</label>
${h.password('password')}<br/>
${h.submit('button', 'Sign In')}
${h.end_form()}
</div></div>