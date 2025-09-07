
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        if other is not None:
            v2 = v1 + other 
        else: 
            v2 = v1
        return v2


m = Model()

 # Inputs to the model
x1  = torch.randn(1,3,64,64)
__output__  = m(x1)