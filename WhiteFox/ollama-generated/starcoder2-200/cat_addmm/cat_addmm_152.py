
class Model(torch.nn.Module):
    def __init__(self, dim=1):
        super().__init__()
 
    def forward(self, x1): 
        v1 = torch.addmm(x1, mat1, mat2) # perform a matrix multiplication of mat1 and mat2 and add it to the input
        v2  = torch.cat([v1], dim=dim) # concatenate the result along dimension dim
        return v2

# Initializing model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 4)
mat1 = torch.randn(500, 800)
mat2 = torch.randn(800, 799)


