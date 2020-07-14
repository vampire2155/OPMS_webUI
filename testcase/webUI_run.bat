@echo off
echo webUI自动化开始......
@echo on

del /f /s /q  G:\Python_webUI\report\tmp\*.json
del /f /s /q  G:\Python_webUI\report\report

@echo off
echo 环境文件删除工作完成，开始运行脚本......
@echo on

cd G:\Python_webUI\testcase
pytest -sq  --alluredir=../report/tmp
allure generate ../report/tmp -o ../report/report --clean

@echo off
echo webUI自动化运行成功
pause