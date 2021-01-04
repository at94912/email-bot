import smtplib
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('abc@gmail.com', '123456') # your gmail address , password
server.sendmail('cds@gmail.com',     # 1 client gmail adderes
                 'dfg@gmail.com',    # 2 client gmail address 
                
                   'hi bro '    # type messege
                    )