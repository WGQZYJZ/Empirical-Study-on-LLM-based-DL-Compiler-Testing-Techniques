
class Model(torch.nn.Module):
    def __init__(self, dim=1):
        super().__init__()
 
    def forward(self, x1):
         mat1  = torch.rand(32, 8) * 5 - 0.5
         mat2  = torch.rand(8, 64) * 5 + 4 # Input 1
         mat3  = torch.rand(32*8*64,) * 7.9
         mat4  = x1.permute(0, 1).reshape(-1)
 
         v1  = torch.addmm(mat1, mat2, mat3) # Input 2
         v2  = torch.cat([v1], dim)         # Output of the model
         return v2

# Initializing the model and setting the concatenation dimension
m  = Model()


# Inputs to the model
mat2  = torch.randn(3*8,64)
mat3  = torch.rand(1*32*64,) * 7.9
__output__  = m(mat2)

