"""
Utility functions to be used by the scripts to manage various resources
and keep the scripts consistent
"""
import json,os,random
class Files:
    def __init__(self,filepath):
        self.filepath=filepath

    def readFile(self):
        data=None
        try:
            f=open(self.filepath,'r')
            data=f.readlines()
            f.close()
        except:
            Messages.error("Could not read file {f}".format(f=self.filepath))
        return data

    def writeFile(self,wdata,append=False):
        data=None
        if(append==True):
            data=self.readFile()
            if(data!=None):
                wdata=str(wdata)+str(data)
            else:
                Messages.error("Could not append data")
                return False
        try:
            f=open(self.filepath,'w')
            f.write(wdata)
            f.close()
            data=True
        except:
            data=False
        return data

    def file_exists():
        if(os.path.isfile(self.filepath)):
            return True
        return False

    def create_file():
        file_path
        while(self.file_exists()==True):
            filename,extension=self.filepath.split(".")
            filename+=str(randrange(1000))
            self.filepath=str(filename)+str(extension)
        try:
            f=open(self.filepath,"w")
            f.close()
            return True
        except:
            Messages.error("Could not create file {f}".format(f=self.filepath))
            return False

class JsonFile:
    @staticmethod
    def loadData(filepath):
        #f=Files(filepath)
        #data=f.readFile()
        with open(filepath,'r') as f:
            try:
                data=json.load(f)
            except:
                Messages.error("Could not generate users")
                data=False
        return data
    @staticmethod
    def fetchField(filepath,field):
        data=JsonFile.loadData(filepath)
        return data[field]

    @staticmethod
    def exportJson(filepath,data,fieldname="users"):
        f=Files(filepath)
        if(f.readFile()!=None):
            json_data=json.dumps({fieldname:data})
            res=f.writeFile(json_data,append=False)
            return JsonFile.handleExportRes(res,data,filepath)
        else:
            res=f.writeFile(data,append=False)
            return JsonFile.handleExportRes(res,data,filepath)

    @staticmethod
    def handleExportRes(res,data,filepath):
        if(res==False):
            Messages.error("Could not export data to file {f}".format(f=filepath))
            return False
        else:
            Messages.success("Exported data {d} to file {f}".format(d=data,f=filepath))
            return True

class Messages:
    c_warning='\033[93m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    @staticmethod
    def error(message,log=False):
        Messages.printMessage(Messages.FAIL,"[Err]",message)
    @staticmethod
    def success(message,log=False):
        Messages.printMessage(Messages.OKGREEN,"[OK]",message)
    @staticmethod
    def warning(message,log=False):
        Messages.printMessage(Messages.c_warning,"[Warning]",message)
    @staticmethod
    def printMessage(mess_col,messagetype,message):
        print("{mc} {mt} {m} {c}".format(mc=mess_col,mt=messagetype,m=message,c=Messages.ENDC))
    @staticmethod
    def cliInput(message):
        Messages.printMessage(Messages.OKCYAN,"{m}\n".format(m=message))
    @staticmethod
    def logEvent(message,logtype="error"):
        l=Logs(logtype)
        l.log(message)

#system maintainence and assesment
class Logs:
    def __init__(self,logtype):
        logtypes=["error","success","warning"]
        if(logtype in logtypes):
            self.logtype=logtype
            self.logsLocation="./Logs"
            self.logFiles={"error":"error.txt","success":"success.txt","warning":"warning.txt"}
        else:
            Messages.error("Logtype {l} is not in logtypes".format(l=logtype),log=False)
    def log(self,message):
        f=Files()
        res=f.writeFile(str(message)+"\n",append=True)
        if(res!=False):
            Messages.printMessage(Messages.FAIL,'[Err]',"Could not log event to logs")

class RandomFigures:
    @staticmethod
    def randomFigure(min=0,max=1000000000):
        return random.randrange(min,max)

#advanced feature for populating websites
"""class Requests:
    @staticmethod
    def post_to_site(url,data):
        pass
    @staticmethod
    def get_from_site(url):
        pass
"""

#filter functionalities for querying data
"""
class JsonFilter:
    @staticmethod
    def equal_to():
        pass
    @staticmethod
    def less_than():
        pass
    @staticmethod
    def not_equal_to():
        pass
    @staticmethod
    def greater_than():
        pass
    #relative to

"""