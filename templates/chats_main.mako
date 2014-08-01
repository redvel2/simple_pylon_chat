<%inherit file="/base.mako" />

<%def name="head_tags()">
  <script src="http://code.jquery.com/jquery-1.11.0.min.js"></script>
  <link type="text/css" rel="stylesheet" href="/style.css"></link>
  <title>New page</title>
</%def>
  <script type="text/javascript">
    $(document).ready(function(){
       $('#sub').click(function(){
         $.getJSON('/chats/json_load', {}, function(json){
         $('#some-id').html('');
         $('#some-id').append('File name '+json.data.name+'<br/>')
         .append('File size '+json.data.size+'<br/>');
         });               
    })
});

  </script>
<h1>Hello ${c.name} !</h1>
<h2>Lets test some JSON data!</h2>
<h2 id="some-id" name="name">Hey</h2>
<div class="sub" id="sub" style="pading:5px;background-color:#555;width:20px;">GO</div>