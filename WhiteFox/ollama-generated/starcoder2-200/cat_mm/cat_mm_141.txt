
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1  = torch.mm(x1, x2) 
        v2  = torch.cat([v1 for i in range(50)], -1) 
        return v2
 
# Initializing the model
m  = Model()

 # Inputs to the model 
_x1  = torch.randn(3, 4, dtype=torch.int64) 
_x2  = torch.randn(3, 50*4, dtype=torch.float64)
__output__  = m(_x1, _x2)

