%#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)
% include('header.tpl', title='Page Title')
<p>User list:</p>
<table border="1">
  <tr>
      <td>User</td>
      <td>Gift</td>
  </tr>
%for row in rows:
  <tr>
  %for r in row:
      <td><a href='/users/{{r.get('uname')}}'>{{r.get('uname')}}</a></td>
      <td><a href='/gifts/{{r.get('idg')}}'>{{r.get('gtype')}}</a></td>
      <td><a href='/users/{{r.get('uname')}}/present/{{r.get('idg')}}'>View</a></td>
  %end
  </tr>
%end
</table>
%if usr == 'Admin':
    <p>If you want to add new present: <a href='/addpresent'>Add</a></p>
%else:
    %if usr != 'None':
        <p><a href='/login'>Log in as Admin</a></p>
    %else:
        <p><a href='/login'>Log in</a></p>
%end

