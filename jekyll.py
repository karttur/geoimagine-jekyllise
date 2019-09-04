'''
Created on 13 Oct 2018

@author: thomasgumbricht
'''


import os
from sys import exit
from xml.etree.ElementTree import Element, Comment, SubElement, tostring
from xml.dom import minidom

from geoimagine.support.karttur_dt import Today
from geoimagine.ancillary import VERSION as ancillaryVersion
from geoimagine.ancillary import metadataD as ancillaryMetaD
from geoimagine.export import VERSION as exportVersion
from geoimagine.export import metadataD as exportMetaD
from geoimagine.extract import VERSION as extractVersion
from geoimagine.extract import metadataD as extractMetaD
from geoimagine.gdalutilities import VERSION as gdalutilitiesVersion
from geoimagine.gdalutilities import metadataD as gdalutilitiesMetaD
from geoimagine.gis import VERSION as gisVersion
from geoimagine.gis import metadataD as gisMetaD
from geoimagine.grace import VERSION as graceVersion
from geoimagine.grace import metadataD as graceMetaD
from geoimagine.image import VERSION as imageVersion
from geoimagine.image import metadataD as imageMetaD
from geoimagine.kartturmain import VERSION as mainVersion
from geoimagine.kartturmain import metadataD as mainMetaD
from geoimagine.ktgraphics import VERSION as graphicsVersion
from geoimagine.ktgraphics import metadataD as graphicsMetaD
from geoimagine.ktnumba import VERSION as numbaVersion
from geoimagine.ktnumba import metadataD as numbaMetaD
from geoimagine.ktpandas import VERSION as pandasVersion
from geoimagine.ktpandas import metadataD as pandasMetaD
from geoimagine.landsat import VERSION as landsatVersion
from geoimagine.landsat import metadataD as landsatMetaD
from geoimagine.layout import VERSION as layoutVersion
from geoimagine.layout import metadataD as layoutMetaD
from geoimagine.mask import VERSION as maskVersion
from geoimagine.mask import metadataD as maskMetaD
from geoimagine.modis import VERSION as modisVersion
from geoimagine.modis import metadataD as modisMetaD
from geoimagine.overlay import VERSION as overlayVersion
from geoimagine.overlay import metadataD as overlayMetaD
#from geoimagine.ortho import VERSION as orthoVersion
#from geoimagine.ortho import metadataD as orthoMetaD
from geoimagine.postgresdb import VERSION as pgVersion
from geoimagine.postgresdb import metadataD as pgMetaD
from geoimagine.region import VERSION as regionVersion
from geoimagine.region import metadataD as regionMetaD
from geoimagine.scalar import VERSION as scalarVersion
from geoimagine.scalar import metadataD as scalarMetaD
from geoimagine.sentinel import VERSION as sentinelVersion
from geoimagine.sentinel import metadataD as sentinelMetaD
from geoimagine.setup_db import VERSION as setupdbVersion
from geoimagine.setup_db import metadataD as setupdbMetaD
from geoimagine.setup_processes import VERSION as setupprocVersion
from geoimagine.setup_processes import metadataD as setupprocMetaD
from geoimagine.smap import VERSION as smapVersion
from geoimagine.smap import metadataD as smapMetaD
#from geoimagine.soilmoisture import VERSION as soilVersion
#from geoimagine.soilmoisture import metadataD as soilMetaD
from geoimagine.support import VERSION as supportVersion
from geoimagine.support import metadataD as supportMetaD
from geoimagine.timeseries import VERSION as timeseriesVersion
from geoimagine.timeseries import metadataD as timeseriesMetaD
from geoimagine.transform import VERSION as transformVersion
from geoimagine.transform import metadataD as transformMetaD
from geoimagine.updatedb import VERSION as updatedbVersion
from geoimagine.updatedb import metadataD as updatedbMetaD
from geoimagine.userproj import VERSION as userprojVersion
from geoimagine.userproj import metadataD as userprojMetaD
from geoimagine.zipper import VERSION as zipVersion
from geoimagine.zipper import metadataD as zipMetaD
  
class GIpackages():
    def __init__(self, FP):
        self.FP = FP
        packageL = ['ancillary', 'export', 'extract', 'gdalutilities', 'gis', 'grace', 'graphics', 'numba', 'image', 'kartturmain', 'ktpandas', 'landsat', 
                    'layout', 'mask', 'modis', 'overlay', 'ortho', 'pg',
                    'region','scalar','sentinel','setupdb','setupproc','smap','soil','support','timeseries',
                    'transform', 'updatedb', 'userproj', 'zipper']
        for pack in packageL:
            if pack == 'ancillary':
                version = ancillaryVersion
                metaD = ancillaryMetaD
            elif pack == 'export':
                version = exportVersion
                metaD = exportMetaD
            elif pack == 'extract':
                version = extractVersion
                metaD = extractMetaD
            elif pack == 'gdalutilities':
                version = gdalutilitiesVersion
                metaD = gdalutilitiesMetaD
            elif pack == 'gis':
                version = gisVersion
                metaD = gisMetaD
            elif pack == 'grace':
                version = graceVersion
                metaD = graceMetaD
            elif pack == 'graphics':
                version = graphicsVersion
                metaD = graphicsMetaD
            elif pack == 'image':
                version = imageVersion
                metaD = imageMetaD
                
            
            elif pack == 'kartturmain':
                version = mainVersion
                metaD = mainMetaD
            elif pack == 'ktpandas':
                version = pandasVersion
                metaD = pandasMetaD
            elif pack == 'landsat':
                version = landsatVersion
                metaD = landsatMetaD
            elif pack == 'layout':
                version = layoutVersion
                metaD = layoutMetaD
            elif pack == 'mask':
                version = maskVersion
                metaD = maskMetaD
            elif pack == 'modis':
                version = modisVersion
                metaD = modisMetaD
            elif pack == 'numba':
                version = numbaVersion
                metaD = numbaMetaD
            
            elif pack == 'ortho':
                pass
                #version = orthoVersion
                #metaD = orthoMetaD
            elif pack == 'overlay':
                version = overlayVersion
                metaD = overlayMetaD
            elif pack == 'pg':
                version = pgVersion
                metaD = pgMetaD
            elif pack == 'region':
                version = regionVersion
                metaD = regionMetaD
            elif pack == 'scalar':
                version = scalarVersion
                metaD = scalarMetaD
            elif pack == 'sentinel':
                version = sentinelVersion
                metaD = sentinelMetaD
            elif pack == 'setupdb':
                version = setupdbVersion
                metaD = setupdbMetaD
            elif pack == 'setupproc':
                version = setupprocVersion
                metaD = setupprocMetaD
            elif pack == 'smap':
                version = smapVersion
                metaD = smapMetaD
            elif pack == 'soil':
                pass
                #version = soilVersion
                #metaD = soilMetaD
            elif pack == 'support':
                version = supportVersion
                metaD = supportMetaD
            elif pack == 'timeseries':
                version = timeseriesVersion
                metaD = timeseriesMetaD
            elif pack == 'transform':
                version = transformVersion
                metaD = transformMetaD
            elif pack == 'updatedb':
                version = updatedbVersion
                metaD = updatedbMetaD
            elif pack == 'userproj':
                version = userprojVersion
                metaD = userprojMetaD
            elif pack == 'zipper':
                version = zipVersion
                metaD = zipMetaD
            self.WritePackagesMD(version, metaD)
  
    def WritePackagesMD(self, version, metaD):
        packageurl = 'package-%(s)s' %{'s': metaD['name'].lower()}
        githuburl = 'geoimagine-%(s)s' %{'s': metaD['name'].lower()}
        if 'image' in metaD:
            image = metaD['image']
        else:
            image = ''
        today = Today().strftime("%Y-%m-%d")
        paramL = ['layout', 'categories', 'date', 'modified', 'packageurl', 'githuburl','packageid','title', 'excerpt', 'version', 'image', 'comments', 'share']
        valueL = ['package', 'package', today, today, packageurl, githuburl,metaD['name'],metaD['name'], metaD['label'], version, image, True, True]
        mdD = dict(zip(paramL,valueL))
        FN = '%(date)s-package-%(n)s.md' %{'date':today,'n':metaD['name'].lower()}
        mdFPN = os.path.join(self.FP,FN)
        
        with open(mdFPN, 'w') as f:
            #json.dump(mdD, f, indent = 0)
            f.write('---\n')
            for key, value in mdD.items():
                f.write('{0}: {1}\n'.format(key, value) )
            f.write('---\n')

class GIprocesses():
    def __init__(self, FP):
        from geoimagine.postgresdb import ManageProcess
        self.session = ManageProcess()
        self.FP = FP
        self.RootProcesses()
        
            
    def RootProcesses(self):
        '''
        '''
        queryD = {}
        rootprocesses = self.session._SelectRootProcess(queryD)
        for rootprocess in rootprocesses:
            print (rootprocess)
            self.WriteRootProcess(rootprocess)
            #Get all the subprocesses for this rootprocess
            self.SubProcesses(rootprocess[0])
    
    def WriteRootProcess(self,rec):  
        rootprocid, title, label = rec      
        url = 'rootproc-%(r)s' %{'r': rootprocid.lower()}
        '''
        if 'image' in metaD:
            image = metaD['image']
        else:
            image = ''
        '''
        today = Today().strftime("%Y-%m-%d")
        paramL = ['layout', 'categories', 'date', 'modified', 'processurl', 'title', 'excerpt', 'image', 'comments', 'share']
        valueL = ['resume', 'rootprocess', today, today, url, rootprocid, label, '', True, True]
        mdD = dict(zip(paramL,valueL))
        FN = '%(date)s-rootproc-%(n)s.md' %{'date':today,'n':rootprocid.lower()}
        mdFPN = os.path.join(self.FP,FN)

        with open(mdFPN, 'w') as f:
            #json.dump(mdD, f, indent = 0)
            f.write('---\n')
            for key, value in mdD.items():
                f.write('{0}: {1}\n'.format(key, value) )
            f.write('---\n')
            
        #Create the directory for this rootprocess
        rootprocSubFolder = 'rootproc-%(s)s' %{'s':rootprocid.lower()}
        rootprocFP = os.path.join(self.FP,rootprocSubFolder)
        if not os.path.exists(rootprocFP):
            os.makedirs(rootprocFP)
        #Create the index.md for this rootpoc
        rootprocFPN = os.path.join(rootprocFP,'index.md')
        today = Today().strftime("%Y-%m-%d")
        paramL = ['layout', 'title', 'excerpt', 'rootprocid', 'search_omit', 'share']
        valueL = ['rootprocess', rootprocid,  label, rootprocid, True, True]
        yamlD = dict(zip(paramL,valueL))

        with open(rootprocFPN, 'w') as f:
            #Write the yaml
            f.write('---\n')
            for key, value in yamlD.items():
                f.write('{0}: {1}\n'.format(key, value) )
            f.write('---\n')
            #Write the code that assembles all subprocesses belonging to this rootprocess
            f.write("<h1 class='foot-description'>Sub processes</h1>\n")
            f.write("<ul class='post-list'>\n")
            f.write("{% for post in site.categories.subprocess %}\n")
            f.write(" {%% if post.rootprocid == '%(rootprocid)s' %%}\n" %{'rootprocid': rootprocid})
            f.write("   {% include subprocess.html post=post %}\n")
            f.write(" {% endif %}\n")
            f.write("{% endfor %}\n")
            f.write("</ul>\n")
       
    def SubProcesses(self, rootprocid):
        '''
        '''
        queryD = {'rootprocid':rootprocid}
        subprocesses = self.session._SelectSubProcess(queryD)
        for subprocess in subprocesses:
            print (subprocess)
            self.WriteSubProcess(subprocess)
            
    def WriteSubProcess(self,rec):
        rootprocid, subprocid, title, label = rec 
        if label == '':
            label = 'No label set yet.'     
        url = 'subproc-%(r)s' %{'r': subprocid}
        today = Today().strftime("%Y-%m-%d")
        paramL = ['layout', 'categories', 'date', 'modified', 'processurl', 'title', 'excerpt', 'image', 'rootprocid','subprocid','author','comments', 'share']
        valueL = ['subprocess', 'subprocess', today, today, url, subprocid, label, '',rootprocid, subprocid,'Thomas Gumbricht', True, True]
        mdD = dict(zip(paramL,valueL))
        FN = '%(date)s-subproc-%(n)s.md' %{'date':today,'n':subprocid}
        mdFPN = os.path.join(self.FP,FN)
        #Get the processparams for this subprocess
        queryD = {'subprocid': subprocid}
        
        paramL = ['rootprocid', 'subprocid', 'version', 'parent', 'element', 'paramid', 'paramtyp', 'tagorattr', 'required',  'defaultvalue', 'bandid']
        processesparams = self.session._SelectProcessParams(queryD)
        processparamL = []
        for proc in processesparams:
            itemL = []
            for item in proc:
                if item == '*':
                    itemL.append('anyid1')
                elif item == '**':
                    itemL.append('anyid2')
                else:
                    itemL.append(item)
                
            processparamL.append(itemL)
  
        tagattrD = {'A':'attribute', 'T':'tag', 'E':'element'}
        with open(mdFPN, 'w') as f:
            f.write('---\n')
            for key, value in mdD.items():
                f.write('{0}: {1}\n'.format(key, value) )
            f.write('---\n')
            #Write the processparameters
            f.write('\n')
            
            f.write("<h1 class='foot-description'>Process XML structure and parameters</h1>")
            f.write('\n')
            
            f.write('```')
            f.write('\n')
            f.write('For details on parameters see the table below\n')
            xmlstr = self.ConstructXML(processparamL)
            f.write(xmlstr)
            f.write('```')
            
            f.write('\n')
            #Blank line before table
            f.write('\n')
            f.write('| paramid | parent | element | type | tagorattr | required | default |\n')
            f.write('|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|\n')
            for processparam in processparamL:
                paramD = dict(zip(paramL,processparam))
   
                paramD['tagorattr'] =  tagattrD[paramD['tagorattr']]
                if paramD['tagorattr'] == 'element':
                    paramD['required'] = '---'
                elif paramD['required'] in ['True','Y','Yes','y']:
                    paramD['required'] = 'yes'
                else:
                    paramD['required'] = 'no'
                if paramD['defaultvalue'] in ['False','No', '']:
                    paramD['defaultvalue'] = '---'
                valueStr = '| %(paramid)s | %(parent)s | %(element)s | %(paramtyp)s | %(tagorattr)s | %(required)s | %(defaultvalue)s |\n' %paramD
                f.write(valueStr)
      
    
    def ConstructXML(self,processesparams):
        '''
        '''
        
        #processtags
        
        root = Element('process')
        
        comment = Comment('Generated from python')
        root.append(comment)
        
        userproj = SubElement(root, 'userproj')

        userproj.set('userid', 'youruserid')
        userproj.set('projectid', 'yourprojectid')
        userproj.set('tractid', 'yourtractid')
        userproj.set('siteid', 'yoursiteid')
        userproj.set('plotid', 'yourplotid')
        userproj.set('system', 'systemid')

        period = SubElement(root, 'period')
        #child_with_tail = SubElement(root, 'child_with_tail')
        period.set('timestep', 'timestep')
        period.set('startyear', 'YYYY')
        period.set('startmonth', 'MM')
        period.set('startday', 'DD')
        period.set('endyear', 'YYYY')
        period.set('endmonth', 'MM')
        period.set('endday', 'DD')
        period.set('seasonstartmonth', 'MM')
        period.set('seasonstartday', 'DD')
        period.set('seasonendmonth', 'MM')
        period.set('seasonendday', 'DD')
        paramL = ['rootprocid', 'subprocid', 'version', 'parent', 'element', 'paramid', 'paramtyp', 'tagorattr', 'required', 'defaultvalue', 'bandid']

        #Loop to get all process parameters
        #parameters = SubElement(root, 'parameters')
        #Loop to set all subElements
        #subElementL = ['srcperiod','dstperiod','srcpath','dstpath','srccomp','dstcomp']
        supProcessD = {}
        for processparam in processesparams:
            paramD = dict(zip(paramL,processparam))
            if paramD['parent'] == 'process':
                if paramD['element'] not in supProcessD:
                    supProcessD[paramD['element']] = SubElement(root, paramD['element'])

        for processparam in processesparams:
            paramD = dict(zip(paramL,processparam))
            if paramD['parent'] == 'process':
                if paramD['tagorattr'] == 'A':
                    if paramD['paramtyp'].lower() in ['text','string']:
                        supProcessD[paramD['element']].set(paramD['paramid'], 'txtstring')
                    elif paramD['paramtyp'].lower()[0:3] == 'int':
                        supProcessD[paramD['element']].set(paramD['paramid'], 'xyz')
                    elif paramD['paramtyp'].lower() in ['real','float']:
                        supProcessD[paramD['element']].set(paramD['paramid'], 'xyz.abc')
                    elif paramD['paramtyp'].lower() in ['bool','boolean']:
                        supProcessD[paramD['element']].set(paramD['paramid'], 'True/False')
                    elif paramD['paramtyp'].lower() == 'date':
                        supProcessD[paramD['element']].set(paramD['paramid'], 'YYYYMMDD')
                    elif paramD['paramtyp'].lower() == 'schema':
                        supProcessD[paramD['element']].set(paramD['paramid'], 'db schema')
                    else:
                        print (paramD['paramtyp'])
                        exit(paramD['paramtyp'])
                elif paramD['tagorattr'] == 'T':
                    tag = SubElement(supProcessD[paramD['element']], paramD['paramid'])
                    tag.text = paramD['paramid']
                elif paramD['tagorattr'] == 'E':
                    pass
                    #tag = SubElement(parameters, paramD['paramid'])
                    #tag.text = paramD['paramid']
                else:
                    print (paramD)
                    exit(paramD)
                    
        subsubProcessD = {}
        for processparam in processesparams:
            paramD = dict(zip(paramL,processparam))
            if paramD['parent'] != 'process':
                if paramD['element'] not in subsubProcessD:
                    #print ('paramD',paramD)
                    #print ('supProcessD',supProcessD.keys())
                    #print (paramD['parent'])
                    if paramD['paramid'] == '*':
                        pass
                    elif paramD['element'] == '*':
                        subsubProcessD['band'] = SubElement(supProcessD[paramD['parent']], paramD['element'])

                    else:
                        subsubProcessD[paramD['element']] = SubElement(supProcessD[paramD['parent']], paramD['element'])
        
        for processparam in processesparams:
            paramD = dict(zip(paramL,processparam))
            if paramD['parent'] != 'process':
                if paramD['tagorattr'] == 'A':
                    if paramD['element'] == '*': paramD['element'] = 'band'
                    if paramD['paramtyp'].lower() in ['text','string']:
                        subsubProcessD[paramD['element']].set(paramD['paramid'], 'txtstring')
                    elif paramD['paramtyp'].lower()[0:3] == 'int':
                        subsubProcessD[paramD['element']].set(paramD['paramid'], 'xyz')
                    elif paramD['paramtyp'].lower() in ['real','float']:
                        subsubProcessD[paramD['element']].set(paramD['paramid'], 'xyz.abc')
                    elif paramD['paramtyp'].lower() in ['bool','boolean']:
                        subsubProcessD[paramD['element']].set(paramD['paramid'], 'True/False')
                    elif paramD['paramtyp'].lower() == 'date':
                        subsubProcessD[paramD['element']].set(paramD['paramid'], 'YYYYMMDD')
                    elif paramD['paramtyp'].lower() == 'schema':
                        subsubProcessD[paramD['element']].set(paramD['paramid'], 'db schema')
                    else:
                        print ('paramtype',paramD['paramtyp'])
                        exit('paramtype',paramD['paramtyp'])
                else:
                    print ('tagorattr',paramD['tagorattr'])
                    print ('paramD',paramD)
                    subsubProcessD[paramD['element']].set(paramD['paramid'], 'childnode (text)')
        return self.prettify(root)

    def prettify(self,elem):
        """Return a pretty-printed XML string for the Element.
        """
        rough_string = tostring(elem, 'utf-8')
        print ('rough_string',rough_string)
        #rough_string.replace('*','any')
        reparsed = minidom.parseString(rough_string)
        return reparsed.toprettyxml(indent="  ")
   
class XmlToHtml():
    def __init__(self, srcPath, dstPath, pattern):
        self.srcPath = srcPath
        self.dstPath = dstPath
        self.pattern = pattern
        if not os.path.exists(dstPath):
            os.makedirs(dstPath)
        self._LoopXMLf()
        
    def _LoopXMLf(self):
        #get all the xml files in the src folder
        import glob
        ymlFPN = os.path.join(self.dstPath,'copy_and_past_to_xml.yml')
        ymlF = open(ymlFPN,"w+")
        
        frontmatterFPN = os.path.join(self.dstPath,'copy_and_past_to_frontmatter.txt')
        frontmatterF = open(frontmatterFPN,"w+")
        
        mdincludeFPN = os.path.join(self.dstPath,'copy_and_past_to_markdown.txt')
        mdincludeF = open(mdincludeFPN,"w+")
        
        search = os.path.join(self.srcPath,'*.xml')
        xmlFL = glob.glob(search)
        xmlFL.sort()

        for xmlFPN in xmlFL:
            if self.pattern in xmlFPN:
                dstFPN = self._OpenDstHtml(xmlFPN)
                ymltxt = os.path.split(dstFPN)[1]
                ymltxt = os.path.splitext(ymltxt)[0]
                frontmatterF.write('%s: %s\n' %(ymltxt,ymltxt))
                
                mdincludeF.write('{%% capture foo %%}{{page.%s}}{%% endcapture %%}\n' %(ymltxt) )
                mdincludeF.write('{%% include xml/%s.html foo=foo %%}\n\n' %(ymltxt) )
                
                ymlF.write( '%s:\n' %(ymltxt) )
                ymlF.write( '    file: %s.xml\n' %(ymltxt) )
                ymlF.write( '    html: %s.html\n' %(ymltxt) )
                ymlF.write( '    id: %s\n' %(ymltxt) )
                ymlF.write( '    author: Thomas Gumbricht\n' )
                ymlF.write( '    caption: null\n' )
                ymlF.write( '    credit: null\n' )
                ymlF.write( '    source: null\n\n' )            
                if not os.path.isfile(dstFPN):
                    self._WriteHtml(xmlFPN,dstFPN)
                self._WriteHtml(xmlFPN,dstFPN)
        ymlF.close()
        mdincludeF.close()
        frontmatterF.close()
            
    def _OpenDstHtml(self,xmlFPN):
        FN = os.path.split(xmlFPN)[1]
        FNbase = os.path.splitext(FN)[0]
        dstFN = '%(FNbase)s.html' %{'FNbase':FNbase}
        dstFPN = os.path.join(dstPath,dstFN)
        return dstFPN
    
    def _WriteHtml(self,xmlFPN,dstFPN):
        dstF = open(dstFPN,"w+")
        with open(xmlFPN) as f:
            content = f.readlines()
        # you may also want to remove whitespace characters like `\n` at the end of each line
        content = [x.strip() for x in content] 
        
        #Set the initial lines
        dstF.write('<button id= "toggle_{{foo}}" onclick="hiddencode(\'{{ foo }}\')">Hide/Show {{ site.data.xml[foo].file }}</button>')
        dstF.write('\n')
        dstF.write('<div id="{{ foo }}" style="display:none">')
        dstF.write('\n')
        dstF.write('{% capture text-capture %}')
        dstF.write('\n')
        dstF.write('{% raw %}')
        dstF.write('\n')
        dstF.write('```')
        dstF.write('\n')
        for row in content:
            dstF.write(row)
            dstF.write('\n')
        dstF.write('```')  
        dstF.write('\n')      
        dstF.write('{% endraw %}')
        dstF.write('\n')
        dstF.write('{% endcapture %}')
        dstF.write('\n')
        dstF.write('{% include widgets/toggle-code.html  toggle-text=text-capture  %}')
        dstF.write('\n')
        dstF.write('</div>')
        dstF.close()
    
    def _WriteHtmlTest(self,xmlFPN,dstFPN):
        dstF = open(dstFPN,"w+")
        with open(xmlFPN) as f:
            content = f.readlines()
        # you may also want to remove whitespace characters like `\n` at the end of each line
        content = [x.strip() for x in content] 
        
        #Set the initial lines
        dstF.write('<button id= "toggle_{{foo}}" onclick="hiddencode(\'{{ foo }}\')">Hide/Show {{ site.data.xml[foo].file }}</button>')
        dstF.write('\n')
        dstF.write('<div id="{{ foo }}" style="display:none">')
        dstF.write('\n')
        
        dstF.write('<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>')
        dstF.write('\n')

        for row in content:
            dstF.write(row)
            dstF.write('\n')
            
        dstF.write('</code></pre></div></div></div>')
        dstF.write('\n')

        dstF.close()
   
if __name__ == "__main__":
    ''' The first part produces pages related to the GeoImagine project itself
    
    FP = '/Users/thomasgumbricht/temp/md'
    #FP = '/Users/thomasgumbricht/jekylltets/geoimagine/_posts/2019
    GIpackages(FP)
    GIprocesses(FP)
    '''
    
    '''This part converts xml coded processes to html files for inclusion in projects as jekyll include liquids
    '''
    pattern = '.'
    srcPath = '/Users/thomasgumbricht/eclipse-workspace/Karttur2019a/geoimagine/projects/doc/AfricaSubSahara/xml'
    dstPath = '/Users/thomasgumbricht/Dropbox/GitHub/soilmoisture-africa/_includes/xml'

    srcPath = '/Users/thomasgumbricht/eclipse-workspace/Karttur2019a/geoimagine/projects/doc/GRACE/xml'
    #dstPath = '/Users/thomasgumbricht/Dropbox/GitHub/geoimagine/_includes/xml'
    srcPath = '/Users/thomasgumbricht/eclipse-workspace/Karttur2019a/geoimagine/projects/doc/TRMM/xml'
    dstPath = '/Volumes/karttur/temp/TRMM/xml'
    srcPath = '/Users/thomasgumbricht/eclipse-workspace/Karttur2019a/geoimagine/projects/doc/VWB/xml'
    dstPath = '/Volumes/karttur/temp/VWB/xml'
    
    srcPath = '/Users/thomasgumbricht/eclipse-workspace/Karttur2019a/geoimagine/projects/doc/ClimateIndexes/xml'
    dstPath = '/Volumes/karttur/temp/ClimateIndexes/xml'
    
    srcPath = '/Users/thomasgumbricht/eclipse-workspace/Karttur2019a/geoimagine/projects/doc/AfricaSubSahara/xml'
    dstPath = '/Users/thomasgumbricht/temp/AfricaSubSahara/TRMM/xml'
    pattern = '_TRMM-'
    
    dstPath = '/Users/thomasgumbricht/temp/AfricaSubSahara/FAOrefET/xml'
    pattern = '_FAOrefET-0'
    
    dstPath = '/Users/thomasgumbricht/temp/AfricaSubSahara/VWB/xml'
    pattern = '_VWB-0'
    
    dstPath = '/Users/thomasgumbricht/temp/AfricaSubSahara/GRACE/xml'
    pattern = '_GRACE-0'
    
    dstPath = '/Users/thomasgumbricht/temp/AfricaSubSahara/TRMM-GRACE/xml'
    pattern = '_TRMM-GRACE-0'
    
    dstPath = '/Users/thomasgumbricht/temp/AfricaSubSahara/VWB-GRACE/xml'
    pattern = '_VWB-GRACE-0'
    
    dstPath = '/Users/thomasgumbricht/temp/AfricaSubSahara/MODIS03/xml'
    pattern = 'MODIS-03'
    
    srcPath = '/Users/thomasgumbricht/eclipse-workspace/Karttur2019a/geoimagine/projects/doc/SMAP/xml/'
    dstPath = '/Users/thomasgumbricht/temp/SMAP/xml'
    pattern = 'SMAP-0'
    
    srcPath = '/Users/thomasgumbricht/eclipse-workspace/Karttur2019a/geoimagine/projects/doc/FAOrefet/xml/'
    dstPath = '/Users/thomasgumbricht/temp/FAOrefet/xml'
    pattern = '-'
    
    srcPath = '/Users/thomasgumbricht/eclipse-workspace/Karttur2019a/geoimagine/projects/doc/MODIS/xml/'
    dstPath = '/Users/thomasgumbricht/temp/MODIS/xml'
    pattern = '-'
    
    XmlToHtml(srcPath, dstPath, pattern)
    
