
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.nn.Linear(20, 4)
        v2  = v1(x1) *  0.5 + ((v1(x1)*v1(x1)) * (torch.ones_like(x1)) * -1.78363789e-1 + torch.zeros_like(x1))
        v3  = v2 
        v4  = v3 
        return v3


# Initializing the model
m = Model()

 # Inputs to the model
 x1  = torch.randn(5, 20)
__output__  = m(x1)