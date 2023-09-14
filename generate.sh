rm output.zip
zip output.zip -r . -x "eb-env/*" "app_env/*" "analysis/*" "venv/*" "output.zip" ".git/*"