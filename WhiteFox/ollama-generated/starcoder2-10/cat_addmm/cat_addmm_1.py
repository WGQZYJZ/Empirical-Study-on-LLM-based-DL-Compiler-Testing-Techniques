
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2  = torch.addmm(x1, mat1, mat2)
        return torch.cat([v2], -1)

# Initializing the model
m  = Model()

 # Inputs to the model
x1  = torch.randn(3, 4096)  # Create a random input tensor
mat1  = torch.randn(8, 512)  # Create two random matrices of sizes (8 x 512) and (768 x 512) respectively.
mat2  = torch.randn(4096, 3, 512)
 
__output__  = m(x1).shape

