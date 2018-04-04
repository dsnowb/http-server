# HTTP Cowsay Server

## GET Endpoints

### /
Returns the contents of index.html

### /cowsay
Returns the contents of cowsay.html
This is a 'descriptive' page

### /cow?msg=VALUE
Displays a koala saying VALUE.
if VALUE includes spaces, VALUE must be enclosed in quotes

#### Example
Endpoint:
/cow?msg="Things"

Response Body:
< Things >
 -------- 
  \
   \
       ___  
     {~._.~}
      ( Y )
     ()~*~()   
     (_)-(_)

## POST Endpoints

### /cow?msg=VALUE
Returns a JSON object. The key is "content", and the value is VALUE passed through cowpy's LukeKoala.milk method.

#### Example
Endpoint:
/cow?msg="Things"

Response Body:
{"content": " ________ \n< Things >\n -------- \n  \\\n   \\          .\n       ___   //\n     {~._.~}// \n      ( Y )K/  \n     ()~*~()   \n     (_)-(_)   \n     Luke    \n     Sywalker\n     koala"}
