% include('header.tpl', title='Page Title')
%if usr != 'None':
    <p>Add new user:</p>
    <form action="/addpresent" method="GET">
        <p> Select User<br/>
        <select name="name">
          %for us in usrs:
            <option>{{us.get('uname')}}</option>
          %end
        </select>
        </p>
        <p>Select Gift<br/>
        <select name="gid">
          %for gf in gfts:
            <option value='{{gf.get('gid')}}'>{{gf.get('gtype')}}</option>
          %end
        </select></p>
        <input type="submit" name="save" value="save">
    </form>
%else:
    <p><a href='/login'>Log in</a></p>
%end
