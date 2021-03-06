# -*-coding:utf-8-*-
import os
import Image
from xml.dom.minidom import parse,parseString

#需要标注面单_几_已标注完成结果
data_path = '/home/nikoong/Algorithm_test/handwritting/data_crop/clean/data1_clean/'
xml_path = '/home/nikoong/dataset/express_list/data_crop/xml/xml1/'
save_path = '/home/nikoong/Algorithm_test/handwritting/data_crop/clean/cut1/'

def endwith(*endstring):
    ends = endstring
    def run(s):
        f = map(s.endswith,ends)
        if True in f:return s
    return run       

def crop_image(image_name,markID,Value,x,y,w,h,save_path):
    image_path = os.path.join(data_path,image_name) 
    ##
    if  0 == w*h:
        return 0
    x1 = x
    y1 = y
    x2 = x + w
    y2 = y + h 
    im = Image.open(image_path)
    #bounding box 
    box =(x1,y1,x2,y2)
    region = im.crop(box)
    image_name_new = image_name.split('.jpg')[0] + "_ID" + markID +"_Value" + Value +".jpg"
    save_path =  os.path.join(save_path , image_name_new)
    region.save(save_path)
    return 0



files = os.listdir(data_path)
end = endwith('.jpg')
image = filter(end,files)
xml = filter(end,files)
for i in range(len(image)):
    xml[i] = os.path.join(xml_path, xml[i].split('.jpg')[0] + '.xml')
for i in range(len(image)):
    if (i%1000 == 0): print i
    doc = parse(xml[i])
    for node in doc.getElementsByTagName('markinfo'):
        markID = node.getAttribute('markID').encode('utf-8')
        value = node.getAttribute('RealValue').encode('utf-8')
        x = node.getAttribute('x').encode('utf-8')
        y = node.getAttribute('y').encode('utf-8')
        w = node.getAttribute('w').encode('utf-8')
        h = node.getAttribute('h').encode('utf-8')
        x = int(x)
        y = int(y)
        w = int(w)
        h = int(h)
        if(value!='0' and value!='1' and value!='2' \
 and value!='3'  and value!='4'  and value!='5' \
 and value!='6'  and value!='7'  and value!='8'  and value!='9'):
            print 'error = ',xml[i]
            print 'error_value = ',value
            continue
        if( w>0 and h>0):
            crop_image(image[i],markID,value,x,y,w,h,save_path)


