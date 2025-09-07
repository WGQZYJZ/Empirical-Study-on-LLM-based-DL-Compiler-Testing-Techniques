
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
    
    def forward(self, x0):
       v0 = self.conv(x0) + 1
       return v0

 # Initializing the model
m  = Model()
 
 # Inputs to the model
x0 = torch.randn(4, 3, 64, 64)
__output__  = m(x0)

