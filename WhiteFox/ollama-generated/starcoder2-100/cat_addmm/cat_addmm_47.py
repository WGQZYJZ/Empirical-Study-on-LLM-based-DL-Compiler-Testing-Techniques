
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
       return torch.addmm(x1, mat1, mat2)
 
# Initializing the model 
m = Model()
 
# Inputs to the model
input = torch.randn(4, 4, requires_grad=True)
mat1 = torch.randn(32, 64, 512, 7, dtype=torch.double, device='cuda')
mat2 = torch.randn(48, 90, 7)
 
__output__, __gradient__  = m(input).sum().backward()

