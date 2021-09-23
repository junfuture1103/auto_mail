from email.mime.text import MIMEText
import smtplib
# 이메일 메시지에 다양한 형식을 중첩하여 담기 위한 객체
from email.mime.multipart import MIMEMultipart

# 이메일 메시지를 이진 데이터로 바꿔주는 인코더
from email import encoders

# 텍스트 형식
from email.mime.text import MIMEText
# 이미지 형식
from email.mime.image import MIMEImage
# 오디오 형식
from email.mime.audio import MIMEAudio

# 위의 모든 객체들을 생성할 수 있는 기본 객체
# MIMEBase(_maintype, _subtype)
# MIMEBase(<메인 타입>, <서브 타입>)
from email.mime.base import MIMEBase
                  
def send_email(smtp_info, msg):
    with smtplib.SMTP(smtp_info["smtp_server"], smtp_info["smtp_port"]) as server:
        # TLS 보안 연결
        server.starttls() 
        # 로그인
        server.login(smtp_info["smtp_user_id"], smtp_info["smtp_user_pw"])

        # 로그인 된 서버에 이메일 전송
        response = server.sendmail(msg['from'], msg['to'], msg.as_string()) # 메시지를 보낼때는 .as_string() 메소드를 사용해서 문자열로 바꿔줍니다.

        # 이메일을 성공적으로 보내면 결과는 {}
        if not response:
            print('이메일을 성공적으로 보냈습니다.')
        else:
            print(response)

smtp_info = dict({"smtp_server" : "smtp.naver.com", # SMTP 서버 주소
                  "smtp_user_id" : "gygh75@naver.com", 
                  "smtp_user_pw" : "11030514aa@", 
                  "smtp_port" : 587}) # SMTP 서버 포트

#####################
# 메일 내용 작성
#####################
title = "첨부파일이 있는 이메일입니다."
content = "메일 내용입니다."
sender = "test@naver.com"
receiver =  "gygh7562@gmail.com" 

# 메일 내용
msg = MIMEText(_text = content, _charset = "utf-8") 
msg['From'] = sender
msg['Subject'] = '메일 발송 시험 (2021.08.05)'
msg['To'] = receiver

# 첨부파일이 추가된 이메일 전송
send_email(smtp_info, msg)