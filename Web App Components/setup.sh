mkdir -p ~/.streamlit/
echo "\
[theme]\n\
primaryColor= '#7792E3' \n\
backgroundColor= '#273346' \n\
secondaryBackgroundColor= '#172c64' \n\
textColor='#ffffff'\n\
font =  'sans serif' \n\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
" > ~/.streamlit/config.toml