'''
There is a default parse task included with the LSST stack, however it may not
be suited to translate the data in your image headers. Usually, you'll need to
write your own translator and load it into the stack. Necam's translators are  saved in:
obs_necam/python/lsst/obs/necam/ingest.py

To load them into the stack, we first import them, then retarget them. 
'''
from lsst.obs.necam.ingest import NecamParseTask
config.parse.retarget(NecamParseTask)

config.parse.translation = {'dataType':'IMGTYPE',
                            'expTime':'EXPTIME',
                            'ccd':'INSTRUME',
                            'frameId':'RUN-ID',
                            'visit':'RUN-ID',
                            'filter':'FILTER',
                            'field':'OBJECT'
                           }

config.parse.translators = {'dateObs':'translate_Date',
                            'taiObs':'translate_Date'}
                            
config.register.visit = ['visit', 'ccd', 'filter','dateObs','taiObs']

config.register.unique = ['visit', 'ccd', 'filter']

config.register.columns = {'frameId':'text',
                           'visit':'text',
                           'ccd':'text',
                           'filter':'text',
                           'dataType':'text',
                           'expTime':'double',
                           'dateObs':'text',
                           'taiObs':'text',
                           'field':'text' }
