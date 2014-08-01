<%inherit file="/base.mako" />

<%def name="head_tags()">
  <link rel="stylesheet" href="main.css">
</%def>

<div class="middle"><div class="middle_content"><h1>Sign up to create chat</h1>

${h.form('/auth/signup',method='post')}
<label>Email</label>${h.text('email')}<br/>
<label>Nickname</label>${h.text('name')}<br/>
<label>Password</label>${h.password('password')}<br/>
Have an account? <a href="/auth/signin">Sign in</a>
${h.submit('button', 'JOIN')}
${h.end_form()}

</div><div class="helper"> </div></div>