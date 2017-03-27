% include('header.tpl', title='Page Title')
%if usr != 'None':
    <p>Add new user:</p>
    <form action="/users/new" method="GET">
        <input type="text" size="30" maxlength="30" name="name">
        <select name="role">
            <option>Admin</option>
            <option>Client</option>
        </select>
        <p>Password:</p>
        <input type="text" size="8" maxlength="8" name="password">
        <input type="submit" name="save" value="save">
    </form>
%else:
    <p><a href='/login'>Log in</a></p>
%end
