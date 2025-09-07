
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, other):
        v2 = self._conv(x1)
        v3  = v2 - other
        return v3
    
    @property
    def conv(self):
        return self._conv

    @_conv.setter
    def conv(self, value):
        self._conv = value


# Initializing the model
m  = Model()
 
# Inputs to the model
x1 = torch.randn(20, 8)
other  = -547 # some constant that is not in the model
 
