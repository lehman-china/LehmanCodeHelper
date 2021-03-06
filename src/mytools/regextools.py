__author__ = 'Administrator'
import re
from src.mytools.commons.utils.common_utils import CommonUtils
string = """

REG:
  SIMPOOL:
    REG:
      {"PROTO":"ESPP/1.1", "MSG":"VREG", "DID":0, "CSEQ":2, "USERNAME":"simpool_test","EXPIRES":0, "NAME":"", "MAX-PORTS":128, "MAC":"6C-EC-EB-61-98-2A", "IP":"192.168.1.73", "VERSION":"SP128-111-007-050-000-000", "SIM-
STATUS":"00000000000000000000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000000000000000000", "NC":2}
    RSP:
      {"PROTO":"ESPP/1.0","MSG":"VREG-ACK","CSEQ":1,"DID":372,"CODE":401,"REASON":"Unauthorized","NONCE":"69902C34E4EFBC06CDBE52B74FF7D1E0"}

    {"PROTO":"ESPP/1.1", "MSG":"VREG", "DID":372, "CSEQ":3, "USERNAME":"simpool_test","EXPIRES":0, "NAME":"", "MAX-PORTS":128, "MAC":"6C-EC-EB-61-98-2A", "IP":"192.168.1.73", "VERSION":"SP128-111-007-050-000-000", "SIM-
STATUS":"00000000000000000000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000000000000000000", "NONCE":"8C025E520F121ADFB70BA7EDAE1508D4","NC":2,"RESPONSE":"34A6AC7CF2A56919B0929BA6A77369CE"}
    {"PROTO":"ESPP/1.0","MSG":"VREG-ACK","CSEQ":2,"DID":372,"CODE":200,"REASON":"OK","EXPIRES":180}


  GOIP:
    REG:
      {"PROTO":"ESCP/1.0", "MSG":"VREG", "DID":373, "CSEQ":3, "EXPIRES":180, "NAME":"", "MAC":"00-30-F1-00-18-CF", "VERSION":"532-475-815-041-100-000", "MAX-PORTS":32, "STATUS":"00000000000000000000000000000000", "IP":"192.168.1.74",
"USERNAME":"goip_test","NONCE":"F75662FE43C9D572A269E725071AAABF","NC":2,"RESPONSE":"1F279F9967A6EEDD10642346B49BC722"}
    RSP:
      {"PROTO":"ESPP/1.0","MSG":"VREG-ACK","CSEQ":3,"DID":373,"CODE":401,"REASON":"Unauthorized","NONCE":"807AAAE7153C2AABAAF3349FE4B32F2D"}

    {"PROTO":"ESCP/1.0", "MSG":"VREG", "DID":373, "CSEQ":4, "EXPIRES":180, "NAME":"", "MAC":"00-30-F1-00-18-CF", "VERSION":"532-475-815-041-100-000", "MAX-PORTS":32, "STATUS":"00000000000000000000000000000000", "IP":"192.168.1.74",
"USERNAME":"goip_test","NONCE":"807AAAE7153C2AABAAF3349FE4B32F2D","NC":2,"RESPONSE":"2473C30DF815962CA2EDB5516C118297"}
    {"PROTO":"ESPP/1.0","MSG":"VREG-ACK","CSEQ":4,"DID":373,"CODE":200,"REASON":"OK","EXPIRES":180}

401:device unauthorized
403:match mac failed or invalid Response
404:device not found
500:DB error



OPEN(GOIP):
   REQ:
     {"PROTO":"ESCP/1.0", "MSG":"VOPEN", "CSEQ":1, "FROM":"57B17FCE", "TO":"0", "CHN-ID":0, "GOIP-SLOT":"goip_test.01", "EXPIRES":120, "CONN-PROTO":"UDPTL 1", "CONN-IP":"192.168.1.74", "CONN-PORT":20002, "CONN-ACKTIME":200, "CONN-
RETRANSTIME":300, "CONN-RETRANSINTVL":200, "CONN-RETRANSCOUNT":7, "MOD-TYPE":"GSM", "MOD-VER":"", "IMEI":"", "GET":"SIM-DATA" , "SESSID":"123"}
   RSP:
     {"PROTO":"ESPP/1.0", "MSG":"VOPEN-ACK", "CSEQ":1, "FROM":3B8B45F5, "TO":0, "GOIP-SLOT":"goip_test.01", "SIM-SLOT":"simpool_test.065", "EXPIRES":120, "CONN-PROTO":"UDPTL 1", "CONN-IP":"192.168.1.92", "CONN-PORT":20098, "CONN-
ACKTIME":200, "CONN-RETRANSTIME":300, "CONN-RETRANSINTVL":200, "CONN-RETRANSCOUNT":7, "MOD-TYPE":"", "MOD-VER":"", "IMEI":"", "GET":""}

VOPENACK
   REQ:
     {"PROTO":"ESPP/1.1", "MSG":"VOPEN-ACK", "CODE":200, "REASON":"OK", "FROM":3B8B45F5, "TO":4353D0CD, "CSEQ":1, , "SESSID":"123"}
   RSP:
     {"PROTO":"ESPP/1.1", "MSG":"VOPEN-ACK", "CODE":200, "REASON":"OK", "FROM":3B8B45F5, "TO":4353D0CD, "CSEQ":1,}




403:Device is offline or Slot is disabled
480:No available SIM
500:Internal server error or DB error



UPDATE(GOIP):
   REQ:
     {"PROTO":"ESCP/1.0", "MSG":"VUPDATE", "CSEQ":55, "FROM":"793313EB", "TO":"2B8B45F4", "TYPE":"KEEPALIVE", "EXPIRES":120, "SIM-NUM":"", "SIM_SIG":31, "SIM-BAL":"0.00", "SESSID":"123"}
   RSP:
     {"PROTO":"ESPP/1.0", "MSG":"VUPDATE-ACK", "CODE":200, "REASON":"OK", "FROM":793313EB, "TO":2B8B45F4, "CSEQ":55, "EXPIRES":120}

200:OK
501:Update error



CLOSE:
  SIMPOOL:
    REQ:
       {"PROTO":"ESPP/1.1", "MSG":"VCLOSE", "CSEQ":2, "FROM":4353D0CF, "TO":3B8B460A, "SESSID":"123"}
    RSP:
       {"PROTO":"ESPP/1.1", "MSG":"VCLOSE-ACK", "CSEQ":2, "FROM":4353D0CF, "TO":3B8B460A, "CODE":200, "REASON":"OK", "SIM-SLOT":"simpool_test.065"}

  GOIP:
    REQ:
      {"PROTO":"ESPP/1.1", "MSG":"VCLOSE", "CSEQ":2, "FROM":4353D0CF, "TO":3B8B460A, "SESSID":"123"}
      {"PROTO":"ESCP/1.0", "MSG":"VCLOSE-ACK", "CSEQ":139, "FROM":"793313F2", "TO":"2B8B4606", "CODE":200, "REASON":"OK", "CHN-ID":0, "GOIP-SLOT":"goip_test.01", "SIM-STATUS":"10 Port is disabled", "BLOCK-TIME":0, "LED-ACTION":"0,0,0"}



PUBLISH:
    {"PROTO":"ESPP/1.1", "MSG":"VPUBLISH", "CSEQ":1, "USERNAME":"simpool_test", "SIM-SLOT":"simpool_test.065", "HAS-SIM":1, "ICCID":"89860113925404104815", "IMSI":"460018772998865", "CONTENT-ENCODING":"GZIP", "CONTENT-TYPE":"APP/SIM-
DATA", "CONTENT-LENGTH":"1142/7246", "TID":123}
    {"PROTO":"ESPP/1.0","MSG":"VPUBLISH-ACK","CSEQ":1,"DID":372,"CODE":200,"REASON":"OK", "TID":123}

200:OK
500:DB error

"""


res = CommonUtils.reg_sub_ex('"([A-Z\-]*?)":', lambda param, child_ma:
                 '"%s":' % child_ma(1).replace("-", "_").lower(), string)
print(res)
