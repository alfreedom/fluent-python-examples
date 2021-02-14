#! /bin/bash

# Example 5-13. Bobo issues a 403 forbidden response if ther are missing function arguments in the request; 
# curl -i is used to dump the headers to standar output.
echo ""
echo "BAD REQUEST---------"
curl -i http://localhost:8080


# Example 5-14. Passing the person parameter is required for an OK response

echo ""
echo "SUCCESS REQUEST---------"
curl -i http://localhost:8080/?person=Alfredo
