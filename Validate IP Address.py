class Solution:
    def val_ip4(self,ip):
        nums = ip.split(".")
        for x in nums:
            if len(x)==0 or len(x) > 3:
                return "Neither"
            else:
                if (len(x)!=1 and x[0] == '0') or  not(x.isdigit()) or int(x)>255:
                    return "Neither"
        return "IPv4"

    def val_ip6(self,ip):
        nums = ip.split(":")
        for x in nums:
            if len(x)==0 or len(x) > 4:
                return "Neither"
            else:
                hex_digits = "0123456789abcdefABCDEF"
                for i in x:
                    if i not in hex_digits:
                        return "Neither"
        return "IPv6"

    def validIPAddress(self, queryIP: str) -> str:
        if queryIP.count('.') == 3:
            return self.val_ip4(queryIP)
        elif queryIP.count(':') == 7:
            return self.val_ip6(queryIP)
        else:
            return "Neither"
            
