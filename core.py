import logging
from typing import Tuple


# Cấu hình logging cơ bản (bạn có thể tùy chỉnh thêm)
logging.basicConfig(filename='core.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


class MyBigNumber:

    def __init__(self) -> None:
        pass

    @staticmethod
    def checkBigNumber(stn: str) -> Tuple[str, int | None]:
        """
        Check if 2 big numbers are valid

        Parameters
        -------
        stn (str): the big number needed to be checked

        Returns
        -------
        int: the position of comma in stn or -1
        """
        logging.info(f"begin check number: {stn}")

        commaPos = None
        removedNum = 0
        result = ""

        for i, char in enumerate(stn):
            if char == "," or char == ".":
                if commaPos != None:
                    logging.error("The number has more than one comma")
                    raise ValueError("The number has more than one comma")

                commaPos = i - removedNum
                result += char

            elif char == "-" and result == "":
                result += char

            elif char < "0" or char > "9":
                logging.error("The number has invalid character")
                raise ValueError("The number has invalid character")

            elif result == "" and char == "0":
                removedNum += 1

            else:
                result += char

        if result == "":
            result = "0"

        logging.info(f"end check number: {result}, commaPos: {commaPos}")
        return result, commaPos

    @staticmethod
    def compare(stn1: str, stn2: str, isDecimal: bool) -> int:
        """
        Compare two big numbers represented as strings.

        Parameters
        -------
        stn1 (str): The first big number string.
        stn2 (str): The second big number string.

        Returns
        -------
        int: -1 if stn1 < stn2, 0 if stn1 == stn2, 1 if stn1 > stn2.
        """
        logging.info(f"begin compare: {stn1} and {stn2}")

        # Compare len if integer
        if len(stn1) > len(stn2) and isDecimal == False:
            logging.info("Compare by length. Result is 1")
            return 1
        elif len(stn1) < len(stn2) and isDecimal == False:
            logging.info("Compare by length. Result is -1")
            return -1

        # Compare each digits
        lenStn1 = len(stn1)
        lenStn2 = len(stn2)

        for i in range(max(lenStn1, lenStn2)):
            if i > lenStn1:
                logging.info(
                    "Compare (decimal) by length when all digits are equal. Result is 1")
                return -1
            elif i > lenStn2:
                logging.info(
                    "Compare (decimal) by length when all digits are equal. Result is -1")
                return 1

            elif stn1[i] > stn2[i]:
                logging.info("Compare by digits. Result is 1")
                return 1
            elif stn1[i] < stn2[i]:
                logging.info("Compare by digits. Result is -1")
                return -1

        logging.info("result compare is equal")
        return 0

    @staticmethod
    def sumDigit(stn1: str, stn2: str, isCarry: bool) -> Tuple[str, bool]:
        """
        Sum 2 digital numbers together

        Parameters
        -------
        stn1 (str): the first digital number
        stn2 (str): the second digital number

        Returns
        -------
        str, bool
        """

        result = int(stn1) + int(stn2)

        if isCarry:
            result += 1
            isCarry = False

        if result >= 10:
            isCarry = True
            result -= 10

        return str(result), isCarry

    @staticmethod
    def subtractDigit(digit1: str, digit2: str, isBorrow: bool) -> Tuple[str, bool]:
        """
        Subtract 2 digital numbers

        Parameters
        -------
        digit1 (str): subtrahend
        digit2 (str): minus
        isBorrow (bool): 

        Returns
        -------
        str, bool
        """
        val1 = int(digit1)
        val2 = int(digit2)
        borrow = 1 if isBorrow else 0
        result = val1 - val2 - borrow

        new_borrow = False
        if result < 0:
            result += 10
            new_borrow = True

        return str(result), new_borrow

    def sumInterger(self, stn1: str, stn2: str, isCarry: bool = False) -> str:
        """
        Sum 2 interger numbers together

        Parameters
        -------
        stn1 (str): the first interger number
        stn2 (str): the second interger number 

        Returns
        -------
        str
        """
        logging.info(f"begin sum interger numbers together: {stn1} and {stn2}")

        curPos1 = len(stn1) - 1
        curPos2 = len(stn2) - 1

        result = ""

        while curPos1 >= 0 or curPos2 >= 0:

            digit1 = stn1[curPos1] if curPos1 >= 0 else "0"
            digit2 = stn2[curPos2] if curPos2 >= 0 else "0"

            sumChar, isCarry = self.sumDigit(digit1, digit2, isCarry)

            result = sumChar + result

            curPos1 -= 1
            curPos2 -= 1

        if isCarry:
            result = "1" + result

        if result == "":
            result = "0"

        logging.info(f"end sum interger numbers together: {result}")
        return result

    def subtractInteger(self, stn1: str, stn2: str, isBorrow: bool = False) -> str:
        """
        Subtract two large integer numbers.

        Parameters
        -------
        stn1 (str): The subtrahend.
        stn2 (str): The minus.
        isBorrow (bool):

        Returns
        -------
        str: The result of the subtraction.
        """
        logging.info(f"begin subtract integer numbers: {stn1} and {stn2}")

        curPos1 = len(stn1) - 1
        curPos2 = len(stn2) - 1

        result = ""

        while curPos1 >= 0 or curPos2 >= 0:
            digit1 = stn1[curPos1] if curPos1 >= 0 else "0"
            digit2 = stn2[curPos2] if curPos2 >= 0 else "0"

            subChar, isBorrow = self.subtractDigit(digit1, digit2, isBorrow)
            result = subChar + result

            curPos1 -= 1
            curPos2 -= 1

        # Remove leading zeros
        for i in range(len(result)):
            if result[i] != "0":
                result = result[i:]
                break

        if result == "":
            result = "0"

        logging.info(f"end subtract integer numbers: {result}")
        return result

    def sumDecimal(self, stn1: str, stn2: str) -> Tuple[str, bool]:
        """
        Sum 2 decimal numbers together

        Parameters
        -------
        stn1 (str): the first decimal number
        stn2 (str): the second decimal number 

        Returns
        -------
        str
        """

        logging.info(f"begin sum decimal numbers together: {stn1} and {stn2}")

        lenStn1 = len(stn1) - 1
        lenStn2 = len(stn2) - 1

        curPos = max(lenStn1, lenStn2)

        isCarry = False
        result = ""

        while curPos >= 0:
            digit1 = stn1[curPos] if curPos <= lenStn1 else "0"
            digit2 = stn2[curPos] if curPos <= lenStn2 else "0"

            sumChar, isCarry = self.sumDigit(digit1, digit2, isCarry)

            if not (result == "" and sumChar == "0"):
                result = sumChar + result

            curPos -= 1

        logging.info(
            f"end sum decimal numbers together: {result}, isCarry {isCarry}")
        return result, isCarry

    def subtractDecimal(self, stn1: str, stn2: str) -> Tuple[str, bool]:
        """
        Subtract two decimal parts of numbers.

        Parameters
        -------
        stn1 (str): The subtrahend.
        stn2 (str): The minus.

        Returns
        -------
        Tuple[str, bool]: 
        """
        logging.info(f"begin subtract decimal numbers: {stn1} and {stn2}")

        lenStn1 = len(stn1) - 1
        lenStn2 = len(stn2) - 1

        curPos = max(lenStn1, lenStn2)

        isBorrow = False
        result = ""

        while curPos >= 0:
            digit1 = stn1[curPos] if curPos <= lenStn1 else "0"
            digit2 = stn2[curPos] if curPos <= lenStn2 else "0"

            subChar, isBorrow = self.subtractDigit(digit1, digit2, isBorrow)

            if not (result == "" and subChar == "0"):
                result = subChar + result

            curPos -= 1

        logging.info(
            f"end subtract decimal numbers: {result}, borrow {isBorrow}")
        return result, isBorrow

    def sum(self, stn1: str, stn2: str) -> str:
        """
        Sum 2 big numbers together

        Parameters
        -------
        stn1 (str): the first big number
        stn2 (str): the second big number 

        Returns
        -------
        str
        """

        logging.info(f"begin sum: {stn1} and {stn2}")

        # Check if stn1 or stn2 is valid
        value1, decimalPoint1 = self.checkBigNumber(stn1)
        value2, decimalPoint2 = self.checkBigNumber(stn2)

        # Check negative or positive
        isPositive1 = stn1[0] != "-"
        isPositive2 = stn2[0] != "-"

        # Split decimal part
        decimal1 = value1[decimalPoint1+1:] if decimalPoint1 != None else "0"
        decimal2 = value2[decimalPoint2+1:] if decimalPoint2 != None else "0"

        # Split integer part
        integer1 = value1[:decimalPoint1] if decimalPoint1 != None else value1
        if isPositive1 == False:
            integer1 = integer1[1:]

        integer2 = value2[:decimalPoint2] if decimalPoint2 != None else value2
        if isPositive2 == False:
            integer2 = integer2[1:]

       # Initialize
        sumedDecimal = ""
        sumedInteger = ""
        isSameSign = isPositive1 == isPositive2
        mainSign = ""  # "" for positive, "-" for negative

        # 2 number have same signs
        if isSameSign:
            if isPositive1 == False:
                mainSign = "-"
            logging.info(f"Sum 2 numbers when have same signs {mainSign}")

            sumedDecimal, isCarry = self.sumDecimal(decimal1, decimal2)

            sumedInteger = self.sumInterger(integer1, integer2, isCarry)

        # 2 number have different signs
        else:
            # Check which number is bigger
            integerComparedResult = self.compare(integer1, integer2, False)

            if integerComparedResult == 1:
                mainSign = "" if isPositive1 else "-"
                logging.info(
                    f"Sum 2 numbers when have different signs and have main sign (check by integer) of the first number {mainSign}")

                sumedDecimal, isBorrow = self.subtractDecimal(
                    decimal1, decimal2)
                sumedInteger = self.subtractInteger(
                    integer1, integer2, isBorrow)
            elif integerComparedResult == -1:
                mainSign = "" if isPositive2 else "-"
                logging.info(
                    f"Sum 2 numbers when have different signs and have main sign (check by integer) of the second number {mainSign}")

                sumedDecimal, isBorrow = self.subtractDecimal(
                    decimal2, decimal1)
                sumedInteger = self.subtractInteger(
                    integer2, integer1, isBorrow)

            elif integerComparedResult == 0:
                decimalComparedResult = self.compare(decimal1, decimal2, True)

                if decimalComparedResult == 1:
                    mainSign = "" if isPositive1 else "-"
                    logging.info(
                        f"Sum 2 numbers when have different signs and have main sign (check by decimal) of the first number {mainSign}")

                    sumedDecimal, isBorrow = self.subtractDecimal(
                        decimal1, decimal2)
                    sumedInteger = self.subtractInteger(
                        integer1, integer2, isBorrow)

                elif decimalComparedResult == -1:
                    mainSign = "" if isPositive2 else "-"
                    logging.info(
                        f"Sum 2 numbers when have different signs and have main sign (check by decimal) of the second number {mainSign}")

                    sumedDecimal, isBorrow = self.subtractDecimal(
                        decimal2, decimal1)
                    sumedInteger = self.subtractInteger(
                        integer2, integer1, isBorrow)

                elif decimalComparedResult == 0:
                    logging.info(f"2 numbers are equal. Result is 0")
                    mainSign = ""
                    sumedDecimal = ""
                    sumedInteger = "0"

        result = sumedInteger

        if len(sumedDecimal) > 0 and sumedDecimal != "0":
            result += "." + sumedDecimal

        result = mainSign + result

        logging.info(f"end sum: {result}")

        return result
