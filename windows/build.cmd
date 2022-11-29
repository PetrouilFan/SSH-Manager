@echo off
python -m pip install pyinstaller
mkdir .tmp
cd .tmp
cls
echo Do you want to include the yaml file with the connections in the exe?
echo If you select yes you wont be able to add or remove connections and you'll need to rebuild the exe
echo If you select no you'll need to have the data.yaml file in the same directory as the exe whenever you run it
set /p include_yaml="(y/n): "
if "%include_yaml%" == "y" (set build_parms=--add-data "../../data.yaml;.") else (set build_parms=)
python -m pyinstaller --noconfirm --onefile --console --icon "../src/icon.ico"  "../../main.py" %build_parms%
xcopy /S /I /Q /Y /F "dist/main.exe" "../"
cd ..
@RMDIR /S /Q .tmp
