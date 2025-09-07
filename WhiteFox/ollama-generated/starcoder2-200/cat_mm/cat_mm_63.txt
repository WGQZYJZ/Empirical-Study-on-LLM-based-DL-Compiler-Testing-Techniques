
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, y2):
        v1  = torch.mm(x1, y2)
        return v1
 
# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(640, 578)
y3 = torch.randn(2991, 31)
__output__  = m(x1, y3)
 
