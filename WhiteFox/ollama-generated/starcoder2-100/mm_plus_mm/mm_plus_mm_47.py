
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        
    def forward(self, x1, x2, x3, x4):
        v1 = torch.mm(x1, x2)
        v2  = torch.mm(v1, x3)
        return torch.mm(v2, x4)

# Initializing the model
m  = Model()

 # Inputs to the model
x1  = torch.randn(8, 9)
x2  = torch.randn(8, 9)
x3  = torch.randn(8, 5)
x4  = torch.randn(5, 7)
 
__output__  = m(x1, x2, x3, x4)

