import re

class CustomUtility:
    @staticmethod
    def validateMsisdn(msisdn: str):
        pattern = r'^233[25][34567]\d{7}$'
        result = re.fullmatch(pattern=pattern, string=msisdn)
        return bool(result)

    @staticmethod
    def apiResponseFormat(success: bool, message: str, data: list):
        return {
            "success": success,
            "message": message,
            "data": data
        }