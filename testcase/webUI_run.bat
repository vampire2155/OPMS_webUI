@echo off
echo webUI�Զ�����ʼ......
@echo on

del /f /s /q  G:\Python_webUI\report\tmp\*.json
del /f /s /q  G:\Python_webUI\report\report

@echo off
echo �����ļ�ɾ��������ɣ���ʼ���нű�......
@echo on

cd G:\Python_webUI\testcase
pytest -sq  --alluredir=../report/tmp
allure generate ../report/tmp -o ../report/report --clean

@echo off
echo webUI�Զ������гɹ�
pause