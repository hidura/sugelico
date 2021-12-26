# -*- coding: utf8 -*-
'''
Created on Jun 24, 2013
sys
@author: hidura
'''

from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from multiprocessing import Process, Queue
import os
import smtplib
import julian
import jdcal

# import astropy.time as astime
# from astropy.time import Time
class general:

    def getTimeFormat(self, time):
        #This just work for datetime.time
        return time.strftime('%H:%M:%S')

    def get_sec(self, time_str):
        h, m, s = str(time_str).split(':')
        return (int(h) * 3600 + int(m) * 60 + int(s))



    def chunkIt(self, seq, num):
        #Create list inside lists
        avg = len(seq) / float(num)
        out = []
        last = 0.0

        while last < len(seq):
            out.append(seq[int(last):int(last + avg)])
            last += avg

        return out

    def sendMail(self, bodyMsg, receiptment, subject=None):
        ##This function, send an email to a client.
        smtpServer = "smtp.webfaction.com"

        server_ssl = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server_ssl.ehlo()  # optional
        sent_from = 'email@address.com'
        subject = 'NO-REPLY' + subject if subject != None else ""
        pwd = "password"
        server_ssl.login(sent_from, pwd)
        email_text = """
        Subject: {}\n\n{}""".format(subject, bodyMsg)

        _attach = MIMEText(email_text.encode('utf-8'), 'html', 'UTF-8')
        msg = MIMEMultipart()
        msg.set_charset('utf8')
        msg['FROM'] = "Sugelico ERP"
        msg['To'] = receiptment.replace("%40", "@")
        msg.attach(_attach)
        server_ssl.sendmail(sent_from, receiptment, msg=msg.as_string())

        server_ssl.quit()

    def date2julian(self, gdate=None):
        _time = None
        if gdate == None:
            gdate = datetime.now()
        else:
            if len(str(gdate).split(" ")) > 0:
                _gdate = str(gdate).split(" ")[0]
                if len(str(gdate).split(" ")) > 1:
                    _time = str(gdate).split(" ")[1]
                gdate = _gdate

            hour = "00"
            minute = "00"
            sec = "00"
            if _time == None:
                _time = hour + ":" + minute + ":" + sec

            format = '%Y/%m/%d'
            if "-" in gdate:
                format = format.replace("/", "-")
            if len(str(gdate).split(" ")) > 1:
                format = '%Y/%m/%d %H:%M:S'

            gdate = datetime.strptime(gdate, format)
        jd = julian.to_jd(gdate, fmt='jd')
        return float(jd)

    def julian2date(self, jdate):
        dt = julian.from_jd(float(jdate))
        return dt


    def sendNotification(self, inputs):
        #Sends a notification of some issue to a type of user
        #Or an User.
        if "type" in inputs:
            None
    def getJulian(self, gDate=None):
        #
        if gDate == None:
            date = datetime.now()
        else:
            if gDate.find(" ") < 0:
                date = datetime.strptime(gDate, "%m/%d/%Y")
            else:
                date = datetime.strptime(gDate, "%m/%d/%Y %H:%M:%S")

        jTplDate = jdcal.jcal2jd(date.year, date.month, date.day)
        return int(jTplDate[0]+jTplDate[1]+float("0."+str(jTplDate[1]).split(".")[1]))


    def checkFolder(self, inputs):
        if "__documentroot__" in inputs:
            if not os.path.exists(inputs["__documentroot__"] + "/resources/site" + "/images/"):
                os.makedirs(inputs["__documentroot__"] + "/resources/site/" + "images/")
            if not os.path.exists(inputs["__documentroot__"] + "/resources/site" + "/ads/"):
                os.makedirs(inputs["__documentroot__"] + "/resources/site/" + "ads/")
            if not os.path.exists(inputs["__documentroot__"] + "/resources/site" + "/products/"):
                os.makedirs(inputs["__documentroot__"] + "/resources/site/" + "products/")


    
    def treatmentLst(self):
        return{1:"Sr.", 2:"Sra.", 3:"Dr.", 4:"Dra.", 5:"Lic.", 6:"Arq.", 7:"Ing."}
    
    def getMainPath(self):


        return "/home/websergroup/webapps/plateacl/htdocs/"
    
    def valEmail(self, mail):
        if mail:
            return True
        
        else:
            return False
    
    def extrctdm(self):
        """In this method the domain is divide in
        all 2 pieces the sub-domain and the domain."""
        # Extracting the domain and the sub domains names
        pathlen = len(self.address) - 1
        dots = 0  # This represents the amount of dot '.' what the system has seems.
        tmpcol = ''  # This variable it's the temporal collector of characters.
        sbdomainList = []  # The sub domain list
        while (pathlen >= 0):
            """This code must not be modified."""
            # In the time that this loop is executing for event point the 
            # loop will append the string collected to a list.
            if self.address[pathlen] == '.':
                if dots == 0:
                    # If the dots is 0 create the tmpcol
                    dots += 1
                    tmpcol = self.address[pathlen] + tmpcol
                else:
                    # Otherwise append to the subdomain list a tmpcol.
                    sbdomainList.append(tmpcol)
                    # Clean the tmpcol var.
                    tmpcol = ''
            else:
                # Collecting the character. in the  
                tmpcol = self.address[pathlen] + tmpcol
            # Reducing one.
            pathlen -= 1
        
        if len(sbdomainList) == 0:
            # Adding the sub-domain to the list 
            sbdomainList.append(tmpcol)
            # And the www as the index.
            sbdomainList.append("www")
        else:
            # Otherwise append the list to the variable.
            sbdomainList.append(tmpcol)
        # Adding to the domain list the sub-domain.
        domainList = [sbdomainList[0]]
        subdomain = ""
        for piece in sbdomainList:
            if piece != sbdomainList[0]:
                subdomain += piece + '.' 
        domainList.append((subdomain[:len(subdomain) - 1]))
        return domainList
    
    
    
    def decodeurl(self, data):
        """This method will 
        decode the arguments."""
        self.dict = {}
        for piece in data.split('&'):
            if piece.find('=') > -1:
                pos = int(piece.find('='))
                self.dict[piece[0:(pos)]] = piece[(pos + 1):len(piece)]
                
      
    
    
    def getInfoEnv(self, environ):
        self.address = str(environ['SERVER_NAME'])  # Extracting the Address.
        domainList = self.extrctdm()  # Separating the domain from the sub domain.
        self.address += str(environ['REQUEST_URI'])
        method = environ['REQUEST_METHOD']  # Extracting the Request method AKA: The method that use the client to communicate.
        
        if method == 'POST':
            # Copy the environ...
            envCp = environ.copy()
            
            strReq = self.pstdtDec(environ, envCp['wsgi.input'])  # Extracting the post-data from the environ all the information.
            if type(strReq).__name__ == 'dict':
                # This means that the post-data comes clean.
                strReq["__domain__"] = domainList[0]
                strReq["__subdomain__"] = domainList[1]
                
                for piece in environ['QUERY_STRING'][2:].split('&'):
                    # Append the request URI as an attribute of the request.
                    strReq[piece.split('=')[0]] = piece.split('=')[1]
                return strReq
            
        # If the method is GET so create the strReq element.
        elif method == 'GET':
            # #Here the strReq is not used the system use the self.dict.
            # self.dict a dictionary that contains the information of the GET.
            strReq = environ['QUERY_STRING']
            
            self.decodeurl(strReq)
            self.dict["__domain__"] = domainList[0]
            self.dict["__subdomain__"] = domainList[0]
            return self.dict    

    def saveFile(self, queue, args):
        #This method will create a process to save a file, returning a name from a
        #hashmap 512 based on a part of the file information.
        data = args[0]
        filename=args[1]

        file = open(filename, "w", encoding="ISO-8859-1")
        file.write(data.decode("ISO-8859-1"))

        file.close()
        queue.put(filename)


    def cmpObj(self, query, cmpdata):
        # This method will create an comparison object, for the system.
        # Receive a dictionaries of lists of dictionaries with the
        # with the params, separated by "and", join to create the
        # filters and added to the query object.
        where = None

        # if "and" in cmpdata:
        #     where=and_
        #     andStr=None
        #     for piece in cmpdata["and"]:
        #         if andStr != None:
        #             andStr+=
        #         andStr
        # print(where)

if __name__ == '__main__':
    general().cmpObj(None, {})

class pproc:
    """This class is building to take the information from
    the byte."""
    
    def __init__(self, environ, wsginp):
        self.formDict = {'__docRoot__':environ["DOCUMENT_ROOT"]}  # Creating the Form dictionary that will content all the fields names and the values!
        
        boundary = environ['CONTENT_TYPE'].split(';')[1].split('=')[1]  # Extracting the number of the mime.
        input = str(wsginp)[1:].strip("''").replace('\\n', '\n')  # Transforming the byte into a string, eliminating the 'b', striping the quotes and replacing the \\n for \n 
        dataSplit = input.split(boundary)  # Separating by the input by the boundary
        self.location = self.formDict['__docRoot__'] + '/tmp/'
        for piece in dataSplit:
            # Using the multiprocessing of Python to extract the data
            q = Queue()
            p = Process(target=self.dataProc, args=(q, piece))
            p.start()
            data = q.get()
            if len(data) == 2:
                self.formDict[data[0]] = data[1]
            p.join()
            
            
            
            
            
    def dataProc(self, queue, field):
        """This method has to extract the information 
        from the field and inserted inside the formDict.
        If is a file it will be saved too!"""
        dataSpl = field[:200].split('\n')[0:3]  # Extracting the header fields
        flStart = 1  # This will be the variable that store the initial point of the file.
        file = None  # This will indicate if in the field is a file.
        binar = None  # This will indicates if is binary or text.
        formList = []
        if len(dataSpl) == 3:
            for info in dataSpl[1].split(';'):
                # Separating the data by the ;
                if 'name' in info.split("=")[0] and 'filename' not in info.split("=")[0]:
                    # If name is in the info that is the fieldNM 
                    fieldNm = info.split("=")[1].strip('""')
                    if '"\\r' in fieldNm:
                        # Cleaning the name
                        fieldNm = fieldNm[:-3]
                if 'filename' in info.split("=")[0]:
                    # If is the filename is a file!
                    if type(info.split("=")[1:]).__name__ == 'list':
                        fileNm = ''
                        for partNM in info.split("=")[1:]:
                            if '"\\r' in partNM:
                                # Cleaning the name of the file.
                                partNM = partNM[:-3]
                            # Collecting the fileNm
                            fileNm += partNM.strip('""')
                    else:
                        # Otherwise the fileNm will be the first position on the list in this split.
                        fileNm = info.split("=")[1]
                    # Appending the file field Name to the formList
                    formList.append(fieldNm)
                    # Doing thr same with the file name.
                    formList.append(fileNm)
                    # Extracting the file type information.
                    flTpInf = dataSpl[2].split(":")[1].split('/')
                    # If text is not on the file type information that means this is a binary file.
                    if 'text' not in flTpInf[0]:
                        # Making binary true
                        binar = True
                        # And creating the file.
                        file = open(self.location + fileNm, 'wb')
                    else:
                        # Otherwise create the file as a text file.
                        file = open(self.location + fileNm, 'w')
            # Is totally necessary that the file has information not a nonetype. 
            if file != None:
                # Here is saving the file!
                part = ''
                # The part is the string that collect the data.
                for piece in dataSpl:
                    # Collecting the data piece by piece.
                    part += field[:field.find(piece) + len(piece)]
                # Now to concrete the saving of the file.
                if binar == True:
                    # This part is for the binary.
                    tmpData = field[field.find(piece) + len(piece):]
                    tmpData = tmpData[4:]  # These represent the 4 first strings \r\n
                    tmpData = tmpData.replace('\r', '\\r')
                    newData = tmpData.replace('\n', '\\n')
                    dataFile = "b'" + newData[:-6] + "'"
                    file.write(eval(dataFile))
                else:
                    # Otherwise save the files as a text.
                    flStart += (len(dataSpl[1]) + len(dataSpl[2]) + 7)
                    data = field[flStart:-1]
                    newData = ''
                    data = data.replace("\\'", "'")
                    for piece in data.split('\\r'):
                        newData += piece.replace('\\t', '\t').expandtabs()
                    file.write(newData[:-2])
                    
                # Close the file.
                file.close()
            else:
                # This part if for extract the data from the fields not from the file.
                part = ''
                # The same thing collecting the data as a string.
                for piece in dataSpl:
                    
                    part += field[:field.find(piece) + len(piece)]
                # Save the same as a newData.
                newData = field[field.find(piece) + len(piece):]
                
                flStart += (len(dataSpl[1]) + len(dataSpl[2]) + 4)
                
                formList.append(fieldNm)
                
                formList.append(field[flStart:-5])
        
        return queue.put(formList)
            
    def sendResult(self):
        """Returning the reuslts!"""
        return (self.formDict)
    

        
        

############################################################
# The errors library starts here.
#
#
#
#
#
#
#


class karpraise(Exception):
    
    def __init__(self, value):
        self.value = value
        
    def __str__(self):
        return repr(self.value)
    
    
    
    
class error:
    
    
    def __init__(self, value):
        print(value.encode('utf8'))

        raise karpraise("KarinApp External library - Problem: " + value)    
