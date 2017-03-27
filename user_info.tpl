%#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)
% include('header.tpl', title='Page Title')
%if usr1 == 'Admin':
    <p>Edit current User info: <a href='/users/{{usr.name}}/edit'>Edit</a></p>
%else:
    %if usr != 'None':
        <p><a href='/login'>Log in as Admin</a></p>
    %else:
        <p><a href='/login'>Log in</a></p>
%end
<p>User {{usr.name}} info:</p>
<table border="1">
  <tr>
      <td>User</td>
      <td>{{usr.name}}</td>
  </tr>
  <tr>
      <td>Role</td>      
      <td>{{usr.role}}</td>
  </tr>
</table>
<p>Gifts of current user</p>
<table border="1">
  <tr>
    %for ls in glist:
      <tr><td><a href='/users/{{usr.name}}/present/{{ls.get('gid')}}'>{{ls.get('gtype')}}</a></td></tr>
    %end
  </tr>
</table>
