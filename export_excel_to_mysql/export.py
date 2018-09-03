# 实现导出excel表格中的数据到mysql数据库
import pymysql # 操作mysql的模块
import openpyxl # xlsx格式对应的操作模块
import time
from datetime import datetime

successList = [] #存储导出成功的数目，用于统计

def readRow(rows):
    conn = pymysql.connect(host="192.168.0.122", port=3306, user="dbuser", passwd="dbpwd", db="dbname", charset="utf8")
    cur = conn.cursor() # 获取游标
    num = 0
    for row in rows:
        id = row[0].value
        name = row[1].value
        username = row[2].value
        password = row[3].value
        date = row[4].value
        status = row[5].value
        if status is None:
            status = ""
        args = (id, name, username, password, date, status)
        try:
            sql = r'''
                insert into vpn (id,name,username,password,date,status)
                values
                (%s,'%s','%s','%s','%s','%s') 
                ''' % args
            cur.execute(sql)
            conn.commit()
            num = num +1
        except Exception as e:
            print(Exception, e,"SQL：%s " % sql)
        else:
            pass
        finally:
            pass

    successList.append(num)
    conn.close()


def excel2Mysql(excelFileName):
    wb = openpyxl.load_workbook(excelFileName)  # 打开excel文件 ；
    sheetList = wb.sheetnames# 获取工作簿所有工作表名
    sheet_obj = sheetList[0] # 不遍历只取第一个工作表
    work_sheet = wb.get_sheet_by_name(sheet_obj)
    rows = work_sheet.rows #获取全部行
    readRow(rows)
    wb.close()

if __name__ == '__main__':
    startTime = datetime.now()
    excelFileName = "/Users/user/Desktop/vpn.xlsx"
    print("[  %s  ] [ 开始导入 %s " % ( time.strftime("%Y-%m-%d %H:%M:%S", time.localtime() ), excelFileName),"文件 ]" )
    excel2Mysql(excelFileName)
    endTime = datetime.now()
    print( "[  %s  ] %s " % ( time.strftime("%Y-%m-%d %H:%M:%S", time.localtime() ) , "[ 导入完毕，总导入：" + str(sum(successList)) + "条 ]") , "[ 用时 %d 秒]" % (endTime-startTime).seconds )
