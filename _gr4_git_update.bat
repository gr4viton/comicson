D:
cd D:\DEV\PYTHON\pyCV\2015_10_11 - pycmulti
git.exe add .
git.exe commit -m "%date% %time%"
git.exe pull -v --no-rebase --progress "origin"
git.exe commit -m "%date% %time% after pull"
git.exe push origin master
python.exe -c "print('\7')" :: BEEP
