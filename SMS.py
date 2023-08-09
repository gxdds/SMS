from twilio.rest import Client

account_sid = 'seuidaqui'
auth_token = 'seutokenaqui'

client = Client(account_sid, auth_token)


remetente = '+numeroaqui' #digite o remetente autenticado no site do TWILIO https://console.twilio.com/?frameUrl=/console
destino = '+numeroaqui' #digite o numero verificado

message = client.messages.create(
    to=destino,
    from_=remetente,
    body='mensagemaqui')

print(message.sid)