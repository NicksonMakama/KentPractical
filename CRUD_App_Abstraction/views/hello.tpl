
<p><h1> This is coming from Database</h1>
<p>
<table border = "2px solid red">
%for item in fromDatabase:
<tr>
   <td> {{item['toyName']}}</td>
   <td> {{item['owner']}}</td>
   <td><a href="/update/{{str(item['id'])}}"/>update</td>
   <td><a href="/delete/{{str(item['id'])}}"/>Delete</td>
</tr>
%end
</table>
<p> <a href = "/insert"> Add an item </a>