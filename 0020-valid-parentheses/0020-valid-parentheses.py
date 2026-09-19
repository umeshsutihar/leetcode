class Solution:
    def isMatched(self, open, close):

        if((open == '(' and close == ')') or
           (open == '[' and close == ']') or
           (open == '{' and close == '}')):
              
            return True
        return False

    def isValid(self, str: str) -> bool:
        st = []
        for i in range(len(str)):
            if str[i] == '(' or str[i] == '[' or str[i] == '{':
                st.append(str[i])
            else:
                if not st:
                    return False
                ch = st[-1]
                st.pop()

                if not self.isMatched(ch, str[i]):
                    return False
        return not st
    
        