
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Linear(4, 8)
    
    def forward(self, x1):
       v0  =  torch.nn.ReLU()(x1)
       v3  =  self.conv(v0)
       v5  =  -2.56 * v3
       v7  =  (v0>0).float() * ((-2.56*v3)+v0) + (-v3) * ~((v0>0).float())
       return v7

# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(8,4)
__output__  = m(x1)