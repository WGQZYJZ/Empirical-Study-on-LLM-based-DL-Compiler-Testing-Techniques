
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1  = torch.addmm(x1, mat1, mat2) 
        return torch.cat([v1], dim=0), x2

# Initializing the model
m  = Model()
 
# Inputs to the model
x1  = torch.randn(3, 500, 500)
x2  = torch.zeros((4,))
__output__, __return_var__  = m(x1, x2)

