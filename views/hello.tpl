%if usernamee =="user":
    Hi {{usernamee}}
%else:
    Hello {{usernamee}}
%end


<h2>These are your List of Pets</h2>

<ul>
%for pet in PetGo:

<li>{{pet["name"]}}
%end
</ul>