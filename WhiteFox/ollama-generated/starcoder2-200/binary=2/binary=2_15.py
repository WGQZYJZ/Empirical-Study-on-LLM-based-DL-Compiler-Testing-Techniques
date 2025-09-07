
class Model(torch.nn.Module):
    def __init__(self,  value=None):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self._init__value_ = value
    
    def forward(self, x1):
        v1  = self.conv(x1)
        if __value__ != None:
            v2 = v1 - __value__
        return v2
        

# Initializing the model
m  = Model()
