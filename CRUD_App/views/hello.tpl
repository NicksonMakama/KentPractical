%if usernamee =="user":
    Hi {{usernamee}}
%else:
    Hello {{usernamee}}
%end
<br>
{{len(petGo)}}
<br>
<h2>These are your List of Pets from an Array</h2>
<table>


%for aPet in petGo:
    
<tr>
<td>{{aPet["name"]}}
<br>
<td>{{aPet["age"]}}

</tr>
%end


</table>
<hr>
<p> This is coming from Database
<p>
<table border = "2px solid red">
%for item in fromDatabase:
<tr>
   <td> {{item['fname']}}</td>
   <td> {{item['kind']}}</td>
   <td><a href="/update/{{str(item['id'])}}"/>update</td>
   <td><a href="/delete/{{str(item['id'])}}"/>Delete</td>
</tr>
%end
</table>
<p> <a href = "/insert"> Add an item </a>