
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, y1, z1, w1):
        v1  = torch.mm(x1,y1) + torch.mm(z1,w1)
        return v1

# Initializing the model
m = Model()

 # Inputs to the model
x2 = torch.randn(3072, 4986)
x3 = torch.randn(3072, 5331)
x4 = torch.randn(3072, 5332)
x5 = torch.randn(3072, 3073)
__output__  = m(x2, x3, x4, x5)

