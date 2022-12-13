class employee:
    def raisee(self):
        raise_rate = 0.1
        return 100 + 100 * raise_rate

class CompEng(employee):
    def raisee(self):
        raise_rate = 0.2
        return 100 + 100 * raise_rate