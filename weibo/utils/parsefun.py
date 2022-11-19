from weibo.log.logPrint import Logger

def logResponse(response):
    log = Logger('weibo/log/logOutput/all.log',level='debug')
    if response.status == 200:
        log.logger.info(str(response.status) + ':' + 'status is normal.')
    elif response.status == 403:
        log.logger.warning(str(response.status) + ':' + 'cookie is banned.')
    elif response.status == 404:
        log.logger.warning(str(response.status) + ':' + 'IP is banned.')
    else:
        log.logger.warning(str(response.status) + ':' + 'other status code.')
        
