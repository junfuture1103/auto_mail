# send_plain.py
import os
import smtplib
 
from email.utils import formataddr
from email.mime.text import MIMEText #메일 제목과 본문을 위한 모듈
from email.mime.multipart import MIMEMultipart

#보내는 사람('이름', '메일 주소')
from_addr = formataddr(('UN사무총장', 'test@kshield.com'))
to_addr = formataddr(('Naver Dochi', 'gygh75@naver.com'))
 
session = None
try:
    # SMTP 세션 생성
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.set_debuglevel(True)
    
    # SMTP 계정 인증 설정
    session.ehlo()
    session.starttls()
    session.login('gygh7562@gmail.com', 'wbfrncdwtwqxzwrz')
 
    # 메일 콘텐츠 설정
    message = MIMEMultipart("alternative")
    
    # 메일 송/수신 옵션 설정
    message.set_charset('utf-8')
    message['From'] = from_addr
    message['To'] = to_addr
    message['Subject'] = '안녕하세요 보안방역반입니다.'
 
    # 메일 콘텐츠 - 내용
    body = '''
    <h2>안녕하세요.</h1>
    <h4>juntheworld입니다.</h1>
    '''
    bodyPart = MIMEText(body, 'html', 'utf-8')
    message.attach( bodyPart )
 
    # 메일 발송
    session.sendmail(from_addr, to_addr, message.as_string())            
    print( 'Successfully sent the mail!!!' )

except Exception as e:
    print( e )
finally:
    if session is not None:
        session.quit()
