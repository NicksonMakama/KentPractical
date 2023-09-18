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
%for item in fromDatabase:
    {{item['fname']}}