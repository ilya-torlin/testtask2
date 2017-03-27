% include('header.tpl', title='Page Title')
%if usr != 'None':
    <p>Add new gift:</p>
    <form action="/gifts/new" method="GET">
        <input type="text" size="30" maxlength="30" name="gtype">
        <input type="submit" name="save" value="save">
    </form>
%else:
    <p><a href='/login'>Log in</a></p>
%end
