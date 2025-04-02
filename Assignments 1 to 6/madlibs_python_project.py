def mad_libs():
   animal=str(input("Enter animal..."))
   name=str(input("Enter name..."))
   verb=str(input("Enter verb..."))
   adjective=str(input("Enter adjective..."))
   place=str(input("Enter place..."))

   story=f"Long time ago, there was a {animal} named {name} . {name} liked to {verb} honey.{name} was a cute little {animal} but he was {adjective}.He enjoyed playing in the {place}.On sunny day he saw a {animal} hive set on fire.He was {adjective} enough to help other {animal} out"
   print (story)
mad_libs()