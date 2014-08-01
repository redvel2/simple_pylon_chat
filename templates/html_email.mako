<%inherit file="/base.mako" />

<%def name="head_tags()">
  <!-- add some head tags here -->
</%def>

<h1 style="margin:auto;">Velcome to our project. Please, open link below and folow instructions</h1>
${h.link_to(c.link, c.link)}