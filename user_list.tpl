%#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)
% include('header.tpl', title='Page Title')
<p>User list: </p>
<table border="1">
  <tr>
      <td>User</td>
      <td>Gift</td>
  </tr>
%for l in lst:
  <tr>
      <td><a href='/users/{{l.get('uname')}}'>{{l.get('uname')}}</a></td>
      <td>{{l.get('urole')}}</td>
  </tr>
%end
</table>
%if usr != 'None':
    <p>If you want to add new User: <a href='/users/new'>Add user</a></p>
%else:
    <p><a href='/login'>Log in</a></p>
%end
