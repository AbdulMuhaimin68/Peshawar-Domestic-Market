@ECHO OFF 
set FLASK_APP=project.app
set FLASK_ENV=development
set DEBUG=true
set JWT_SECRET_KEY="pakistandomesticmarket"

SET DB_NAME=pdm
SET DB_URL=localhost
SET DB_USER=root
SET DB_PWD=smartforum123
SET DB_PORT=3306

CMD /k "python -B runDebug.py"
