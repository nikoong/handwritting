import methods

txtlist=methods.txt2list('/home/nikoong/Algorithm_test/handwritting/data/txt/finish/balance_val.txt')

for i in range(len(txtlist)):
    if len(txtlist[i].split('finish'))!= 1:
        txtlist[i] = txtlist[i].split('finish')[0]+'onlyresize'+txtlist[i].split('finish',)[1]

methods.list2txt(txtlist,'/home/nikoong/Algorithm_test/handwritting/data/txt/onlyresize/balance_val.txt')