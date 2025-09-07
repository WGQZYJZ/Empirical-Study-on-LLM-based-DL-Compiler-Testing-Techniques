
class Model(torch.nn.Module):
    def __init__(self, dim=0):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.addmm(x1, mat1, mat2)
        v2  = torch.cat([v1], dim)
        return v2

# Initializing the model
m = Model()


# Inputs to the model
mat1 = torch.randn(64 * 3980)
mat2 = torch.randn(750, 64*3980)
input = torch.randn(1, 64*3980)
x1= torch.zeros([1])
 
