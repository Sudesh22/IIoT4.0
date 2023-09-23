class Mail:
    changePassword = {
        "mailBody" : '''
                        <!DOCTYPE html>

                        <head>
                            <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
                            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
                            <title>OTP for Login</title>
                        </head>

                        <body
                            style="width:80%; height:100%; margin:0; padding:32px; font: normal normal normal 10px/15px Arial,sans-serif; color:#333; background-color:#f1f1f1; -webkit-text-size-adjust:100%; -ms-text-size-adjust:100%;">
                            <table class="email-wrapper"
                                style="width:100%; height:100%; margin:auto; padding:0; text-align:center; vertical-align:middle; border-spacing:0; border-collapse:collapse;">
                                <tr>
                                    <td>
                                        <table class="email-layout"
                                            style="width:500px; height:200px; padding:0; vertical-align:middle; border-spacing:0px;">
                                            
                                            <tbody class="email-body">
                                                <tr>
                                                    <td style="text-align:left;">
                                                        <div
                                                            style="padding:21px 32px; background-color:#fff; border-bottom:2px solid #e1e1e1; border-radius:3px;">
                                                            <h1 style="text-align:center; color: coral;">IOconnect</h1>
                                                            <p style="text-align : center; font-size: 1.1rem; font-weight:bold;">
                                                            Hi  {name}, lets reset your password 🔑!
                                                            </p>
                                                            <h1 style="text-align: center;">{token}</h1> 
                                                            <p style="text-align: center;">Here is your OTP verification code</p>
                                                            <p style="text-align: center;">This OTP is valid for only 10 min</p>
                                                            <p style="text-align: center;">If you didn't ask to reset your password, <a href="#" style="text-decoration: none;">let us know</a></p>
                                                        </div>
                                                    </td>
                                                </tr>
                                            </tbody>

                                            <tfoot class="email-footer" style="text-align:center; font-weight:normal;">
                                                <tr>
                                                    <td style="padding-top:32px;">
                                                        <div style="color:#999;">
                                                            <a href="" target="_blank"
                                                                style="text-decoration:none; color:#446cb3 !important;">Get in touch</a> |
                                                            <a href="" target="_blank"
                                                                style="text-decoration:none; color:#446cb3 !important;">FAQs</a> |
                                                            <a href="" target="_blank"
                                                                style="text-decoration:none; color:#446cb3 !important;">Terms and Conditions</a>
                                                        </div>
                                                        <small style="font-size:12px; color:#999;">© IOconnect 2023 All rights reserved<small>
                                                    </td>
                                                </tr>
                                            </tfoot>
                                        </table>
                                    </td>
                                </tr>
                            </table>
                        </body>
                        </html>
                        ''',
        "subject" : "OTP for Login - {token}"
    }

    passwordSuccess = {
        "mailBody" : '''
                        <!DOCTYPE html>

                <head>
                    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
                    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
                    <title>OTP for Login</title>
                </head>

                <body
                    style="width:80%; height:100%; margin:0; padding:32px; font: normal normal normal 10px/15px Arial,sans-serif; color:#333; background-color:#f1f1f1; -webkit-text-size-adjust:100%; -ms-text-size-adjust:100%;">
                    <table class="email-wrapper"
                        style="width:100%; height:100%; margin:auto; padding:0; text-align:center; vertical-align:middle; border-spacing:0; border-collapse:collapse;">
                        <tr>
                            <td>
                                <table class="email-layout"
                                    style="width:550px; height:200px; padding:0; vertical-align:middle; border-spacing:0px;">

                                    <tbody class="email-body">
                                        <tr>
                                            <td style="text-align:left;">
                                                <div
                                                    style="padding:21px 32px; background-color:#fff; border-bottom:2px solid #e1e1e1; border-radius:3px;">
                                                    <h1 style="text-align:center; color: coral;">IOconnect</h1>
                                                    <p style="text-align : center; font-size: 1.1rem; font-weight:bold;">
                                                        Hi {name}, your password was reset successfully ✅!
                                                    </p>
                                                    <p style="text-align: center;">This is a confirmation that the password for your IOconnect account has just been changed</p>
                                                    <p style="text-align: center;">If you didn't change your password, <a href="#" style="text-decoration: none;">let us know</a></p>
                                                    <p style="text-align: center;">If you're having trouble, please refer to the <a href="#" style="text-decoration: none;">IOconnect Help Center</a></p>
                                                </div>
                                            </td>
                                        </tr>
                                    </tbody>

                                    <tfoot class="email-footer" style="text-align:center; font-weight:normal;">
                                        <tr>
                                            <td style="padding-top:32px;">
                                                <div style="color:#999;">
                                                    <a href="" target="_blank"
                                                        style="text-decoration:none; color:#446cb3 !important;">Get in touch</a> |
                                                    <a href="" target="_blank"
                                                        style="text-decoration:none; color:#446cb3 !important;">FAQs</a> |
                                                    <a href="" target="_blank"
                                                        style="text-decoration:none; color:#446cb3 !important;">Terms and Conditions</a>
                                                </div>
                                                <small style="font-size:12px; color:#999;">© IOconnect 2023 All rights reserved<small>
                                            </td>
                                        </tr>
                                    </tfoot>
                                </table>
                            </td>
                        </tr>
                    </table>
                </body>
                </html>''',
        "subject" : "Password Reset Successfully"
    }