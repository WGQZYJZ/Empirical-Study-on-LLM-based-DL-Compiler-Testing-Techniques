
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v0  = torch.cat([x1, x1], dim=3) 
        return v0

 # Initializing the model
 m  = Model()
 
# Inputs to the model
 x1  = torch.randn(64, 8, 56, 56) 
 x2  = torch.randn(64, 8, 56, 56)
__output__   = m(x1, x2)

