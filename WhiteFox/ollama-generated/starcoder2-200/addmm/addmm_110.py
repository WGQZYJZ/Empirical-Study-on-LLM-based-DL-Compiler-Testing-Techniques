
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2) + x3
        return v1
 
# Initializing the model
m  = Model()

 # Inputs to the model
x1 = torch.randn(50, 64)
inp = torch.randn(78, 64)
x2 = torch.randn(78, 32)
__output__  = m(x1, x2, inp)

 