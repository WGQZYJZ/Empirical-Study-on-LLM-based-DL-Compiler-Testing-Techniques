
class Model(torch.nn.Module):
    def __init__(self, mat1_, mat2_, dim):
        super().__init__()
        self.mat1  = torch.tensor(mat1_)
        self.mat2  = torch.tensor(mat2_)
 
    def forward(self, x0): 
        v0  = torch.addmm(x0, self.mat1, self.mat2) # Add two tensors multiplied by each other and then pass the result to another layer
        v1  = torch.cat([v0], dim)                   # Concatenate along a specified dimension
        return v1


# Initializing the model
m = Model(mat1_, mat2_, dim)


# Inputs to the model
x0 = torch.randn(3, 8)
__output__  = m(x0)