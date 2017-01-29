class ModernPrepod:
    def __init__(self, **kwargs):
        for k,v in kwargs.items():
            setattr(self, k, v)

    def __str__(self):
        return ' '.join(map(str,self.__dict__.values()))