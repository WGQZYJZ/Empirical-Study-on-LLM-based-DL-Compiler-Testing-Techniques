
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v0  = self.linear(x1) 
        return v0 + other
        
# Initializing the model
m = Model()
 
other  = torch.randn((42,)) # Arbitrary tensor
 
# Inputs to the model
x1  = torch.randn(7, 32, 64, 8)


__output__  = m(x1)

