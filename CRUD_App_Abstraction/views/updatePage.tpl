<h3> Update here</h3>
<form action = "/updateQuery" method="POST">
        <input type="hidden" name = "toyId" value="{{str(fromDatabase['id'])}}"/> <br><br>
    Toy Name: <input name = "toyName" value="{{fromDatabase['toyName']}}"/> <br><br>
    Owner: <input name = "toyOwner" value="{{fromDatabase['owner']}}"/> <br>

    <button type = "submit"> Update </button>
</form>