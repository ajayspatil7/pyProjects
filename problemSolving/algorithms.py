

class Algorithms:

    def bubbleSort(self, sequence: list) -> list:
        n = len(sequence)
        for i in range(n - 1):
            for j in range(n - 1 - i):
                if sequence[j] > sequence[j + 1]:
                    tempArray = sequence[j]
                    sequence[j] = sequence[j + 1]
                    sequence[j + 1] = tempArray
        return sequence

    def primeNumbers(self, lowerRange: int, upperRange: int):

        for num in range(lowerRange, upperRange + 1):
            if num > 1:
                for i in range(2, num):
                    if num % i == 0:
                        break
                    else:
                        print(num)
                        break

    def checkIsPrimeOrNot(self, integerToCheck: int):
        num = integerToCheck
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    return False
            else:
                return True
        else:
            return False

    def isPalindrome(self, string: str):
        if string == string[:: -1]:
            return True
        else:
            return False

    def reversedString(self, string: str):
        return string[:: -1]

algo = Algorithms()
soln = algo.isPalindrome("hannah")
print(soln)