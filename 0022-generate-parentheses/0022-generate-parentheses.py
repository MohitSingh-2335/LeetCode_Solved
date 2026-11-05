class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        if n == 1: return ["()"]
        n -= 1
        result = []

        def func(open, close, para):
            if not open and not close:
                result.append(para + ')')
                return

            if open > 0:
                func(open - 1, close, para + '(')

            if close >= open:
                func(open, close - 1, para + ')')

        func(n, n, '(')

        return result