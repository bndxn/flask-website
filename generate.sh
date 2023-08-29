rm output.zip
zip output.zip -r . -x "eb-env/*" "app_env/*" "analysis/*" "output.zip" ".git/*"