%#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)
% include('header.tpl', title='Page Title')
<p>Gift Info:</p>
<table border="1">
    %for ls in gf:
      <tr>
        <td>{{ls.get('gid')}}</td>
        <td>{{ls.get('gtype')}}</td>
      </tr>
    %end
</table>
