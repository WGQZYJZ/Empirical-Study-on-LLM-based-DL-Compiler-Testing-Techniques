
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, x3, x4):
        v1  = torch.mm(x1, x2)
        v2  = torch.mm(x3, x4)
        return v1 + v2

# Initializing the model
m  = Model()
 
# Inputs to the model
x1 = torch.randn(8, 640)
x2 = torch.randn(640, 975)
x3 = torch.randn(8, 975)
x4 = torch.randn(975, 975)
__output__  = m(x1, x2, x3, x4)

