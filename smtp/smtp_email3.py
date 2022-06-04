import smtplib
from email.message import EmailMessage
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

sender = 'ninanooo@gmail.com'
recipient = 'daeheekim@sch.ac.kr'
password = '앱 비밀번호'

msg = EmailMessage()
msg['Subject'] = "HTML 메시지 전송"
msg['From'] = sender
msg['To'] = ('daeheekim@sch.ac.kr', 'ninanooo@gmail.com')
# HTML 메시지 작성하기
content_id = 'my_image1' # 이미지 등의 컨텐츠를 연결하기 위한 id
msg.add_alternative('''\ # multipart/alternative 객체를 만들어 본문에 추가함
<html>
    <head></head>
    <body>
        <p>안녕하세요.</p>
        <p>순천향대학교 김대희입니다.</p>
        <p>아래 사이트 확인 부탁 드립니다.</p>
        <p>
            <a href=https://home.sch.ac.kr/iot/>
            순천향대학교 사물인터넷학과
            </a>
        </p>
        <p>감사합니다.</p>
        <img src="cid:{cid}" />
    </body>
</html>
'''.format(cid=content_id), subtype='html')

# HTML 메시지의 해당 부분에 이미지 추가하기
with open("iot.png", 'rb') as img:
    msg.get_payload()[0].add_related(img.read(), maintype='image', subtype='png', cid=content_id)

# 보내는 메시지 저장하기
with open('outgoing.msg', 'wb') as f:
    f.write(bytes(msg))
    
s = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
s.ehlo()
s.starttls()
s.login(sender, password)
s.send_message(msg)
s.quit()