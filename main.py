from Service.service import service

try:
    servico = service()

except OSError as err:
    print("OS error: {0}".format(err))