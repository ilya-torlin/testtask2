% include('header.tpl', title='Page Title')
%if usr1 != 'None':
    <p>Add new user:</p>
    <form action="/users/{{usr.name}}/edit" method="GET">
        <input type="text" size="30" maxlength="30" name="name" value="{{usr.name}}">
        <select name="role">
            %if usr.role == 'Admin':
                <option selected>Admin</option>
                <option>Client</option>
            %else:
                <option>Admin</option>
                <option selected>Client</option>
            %end
        </select>
        <p>Password:</p>
        <input type="text" size="8" maxlength="8" name="password" value="{{usr.password}}">
        <input type="submit" name="save" value="save">
    </form>
%else:
    <p><a href='/login'>Log in</a></p>
%end
