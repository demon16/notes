import requests

import werkzeug.datastructures
data = werkzeug.datastructures.MultiDict([
                ('GuestAges[]', 30),('GuestAges[]', 30),
                ('ShipCode', 'QN'),
                ('SailDate', '2018-02-08'),
                ('PackageId', 'QN04I347'),
                ('StateroomType', 'INTERIOR'),
                ('AgencyId', 333545)])
url = 'http://www.rcclchina.com.cn/api/Rccl.Booking/StateroomCategoryApi'


headers = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'Cookie': 'ASP.NET_SessionId=u0trflsbvkj431fjcfdl2mni; Hm_lvt_25fb4a4b0a15e6d526ef631c8f3d2889=1516527225; gr_user_id=87bc28ac-088c-41df-a10a-82e9e53fce85; gr_session_id_921e89cb41ad945c=50225fc9-7c01-44dc-a222-0b9ac6f00947; s_fid=3EC9200C013585EC-342537FCDDC5E866; s_cm=bzclk.baidu.comOther%20Natural%20Referrersundefined; s_cc=true; LXB_REFER=bzclk.baidu.com; s_evar66cvp=%5B%5B%27Other%2520Referrers-bzclk.baidu.com%27%2C%271516527244477%27%5D%5D; s_evar68cvp=%5B%5B%27Other%2520Referrers%27%2C%271516527244478%27%5D%5D; __RequestVerificationToken=SphuVvSk8JOLw2D_ltKsuJOJNbtWxBIH9AOzY3M-wK72h6QWrS_BHby-i19Sb9KYiCi9TGSoOD9ihknuvTq2ezRa1zX8CyYxMFRPp78CtB81; rcuuid=6d518291-0677-47ed-adf5-9663662fd79f; CruiseIds=150853; s_cp_url=%E7%AB%8B%E5%8D%B3%E9%A2%84%E8%AE%A2%7E..%2Frccl.booking%2Fbooking%2Fbooking%3Fsaildate%3D2018-03-08%26shipcode%3Dqn; gpv_pn=rcl-chn%3A%20rccl.booking%3A%20booking%3A%20booking; s_sq=%5B%5BB%5D%5D; Hm_lpvt_25fb4a4b0a15e6d526ef631c8f3d2889=1516530289; utag_main=v_id:0161181107aa006b2555b83b241404069005806100bd0$_sn:2$_ss:0$_st:1516532089848$vapi_domain:rcclchina.com.cn$ses_id:1516530177359%3Bexp-session$_pn:3%3Bexp-session; s_nr=1516530289864-Repeat'
}

r = requests.post(url, data=data, headers=headers)