
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1  = torch.mm(x1, x2) 
        v2  = torch.cat([v1] * len(v1), dim=0)
        return v2

# Initializing the model
m  = Model()

 # Inputs to the model
x1 = torch.randn(89374, 56483)
x2 = torch.randn(56483, 23567) 
 __output__= m(x1, x2)

 