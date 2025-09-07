
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = self.linear(x1) + self.__other__
        return v1
 
 
# Initializing the model
m  = Model()

 # Inputs to the model 
 m.linear   = torch.nn.Linear(32*32*8, 50)
 
 x1  = torch.randn(64, 32 * 32 * 8)
 
__output__  = m(x1)
