%#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)
% include('header.tpl', title='Page Title')
<p>Info User & Gift:</p>
<table border="1">
  <tr>
      <td>User</td>
      <td>User Role</td>
      <td>Gift</td>
  </tr>
%for l in lsinfo:
  <tr>
      <td><a href='/users/{{l.get('uname')}}'>{{l.get('uname')}}</a></td>
      <td>{{l.get('urole')}}</td>
      <td><a href='/gifts/{{l.get('gid')}}'>{{l.get('gtype')}}</td>
  </tr>
%end
</table>
