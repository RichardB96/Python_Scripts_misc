import os
from os import path

outputList = []

Sci_path = '/media/rb20/Al10Tb/BioBank_Batches_RB/'
for batch in os.listdir(Sci_path):
    Sci_path_batch = Sci_path + str(batch) + '/'
    for case in os.listdir(Sci_path_batch):

        tempLVEDV = None
        tempRVEDV = None
        tempLVESV = None
        tempRVESV = None
        tempLVEF = None
        tempRVEF = None
        tempLVMyoMassES = None
        tempLVMyoMassED = None
        tempRVMyoMassES = None
        tempRVMyoMassED = None

        if path.exists(Sci_path_batch+str(case)+'/'+case+'_con_sciReport.txt'):
            SciFile = open(Sci_path_batch+str(case)+'/'+case+'_con_sciReport.txt','r',encoding='utf-16')
            returning = False
            side = ''
            outdict = {}
            for line in SciFile:
                if line == '\n':
                    pass
                else:
                    if 'SAX3D LV & RV Function (1)' in line:
                        returning = True
                    if 'SAX 3D Function (ml)' in line:
                        returning = False
                    if 'Clinical Results LV' in line:
                        side = 'left'
                    if 'Clinical Results RV' in line:
                        side = 'right'

                    if line.split()[0]=='EDV' and returning==True:
                        if side == 'left':
                            tempLVEDV = line.split()[1]
                        elif side == 'right':
                           tempRVEDV = line.split()[1]
                    if line.split()[0]=='ESV' and returning==True:
                        if side == 'left':
                            tempLVESV = line.split()[1]
                        elif side == 'right':
                            tempRVESV = line.split()[1]
                    if line.split()[0] == 'EF' and returning == True:
                        if side == 'left':
                            tempLVEF = line.split()[1]
                        elif side == 'right':
                            tempRVEF = line.split()[1]
                    if line.split()[0] == 'MyoMass_diast' and returning == True:
                        if side == 'left':
                            tempLVMyoMassED = line.split()[1]
                        elif side == 'right':
                            tempRVMyoMassED = line.split()[1]
                    if line.split()[0] == 'MyoMass_syst' and returning == True:
                        if side == 'left':
                            tempLVMyoMassES = line.split()[1]
                        elif side == 'right':
                            tempRVMyoMassES = line.split()[1]

            outdict = {'Patient':case,'Batch':batch,'LVEDV':tempLVEDV, 'RVEDV':tempRVEDV, 'LVESV':tempLVESV, 'RVESV':tempRVESV,'LVEF':tempLVEF,'RVEF':tempRVEF, 'LVMyoMassES':tempLVMyoMassES,'RVMyoMassES':tempRVMyoMassES,'LVMyoMassED':tempLVMyoMassED,'RVMyoMassED':tempRVMyoMassED}
            outputList.append(outdict)
        else:
            print(case+' from batch ' +batch + ' is incomplete.')

outfile = open("BioBank_data_summary.csv","w+")
outfile.write('Patient,Batch,LVEDV,RVEDV,LVESV,RVESV,LVEF,RVEF,LVMyoMassES,RVMyoMassES,LVMyoMassED,RVMyoMassED\n')
for x in outputList:
    outfile.write(str(list(x.values())).replace("'","")[1:-1] + '\n')
