import os
#coding:utf-8

path='/F/图片/上海/20080920-崇明/'
# file names
filenames=os.listdir(path)
#file list
filelist=[]
# file map
filemap={}
for name1 in range(0,len(filenames)):
    #get the file's  name
    oldname= filenames[name1]
    # just deal with files 
    if os.path.isdir(path+oldname):
        continue
    
    elif os.path.exists(path+'.DS_Store'):
        os.remove(path+'.DS_Store')
        
    else:
        #print oldname
    
        #get the file's modify time
        time1= os.path.getmtime(path+oldname)
        #print time1
    
        #get the map time VS  name
        filemap[time1]=oldname
    
        #add the time to the shuzu 
        filelist.append(time1)
    
        # sort from small to big by time
        filelist.sort()

#the file list from small to big  
#print filelist

for i in range(0,len(filelist)):
    startfile=filelist[i]  
    #print filemap[startfile]
    filenamestr=filemap[startfile] 
    
    #get the file type  
    filestrafter1= filenamestr.split('.')
    filenamestr2 = filestrafter1[1]
    
    #number + the type ,eg:jpg  
    newname= str(i)+'.'+filenamestr2

    # rename 
    os.rename(path+filenamestr, path+newname)

'''out = open ('/D/testtest/pri.txt','w')
out.write('colin')
out.close
'''
    