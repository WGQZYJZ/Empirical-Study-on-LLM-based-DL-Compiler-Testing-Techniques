
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1  = torch.mm(x1, x2)
        return v1 + v1

# Initializing the model
m  = Model()

 # Inputs to the model
a = torch.randn(3, 4)
b = torch.randn(5, 6)
 
__output__  = m(a, b)



