%#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)
% include('header.tpl', title='Page Title')
<p>Gift List:</p>
<table border="1">
    %for ls in glst:
      <tr><td><a href='/gifts/{{ls.get('gid')}}'>{{ls.get('gtype')}}</a></td></tr>
    %end
</table>
%if usr != 'None':
    <p>If you want to add new Gift: <a href='/gifts/new'>Add gift</a></p>
%else:
    <p><a href='/login'>Log in</a></p>
%end
