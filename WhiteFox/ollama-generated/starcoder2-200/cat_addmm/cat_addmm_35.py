
class Model(torch.nn.Module):
    def __init__(self, dim=1):
        super().__init__()
        self.mat2 = torch.randn(3, 4)
        self.mat1 = torch.randn(5, 3)
 
    def forward(self, x1):
        v1 = torch.addmm(x1, mat1, mat2) # Matrix multiplication is performed on a 3x4 and 5x3 tensors.
        return torch.cat([v1], dim)


# Initializing the model
m = Model()
dim  = 0 # Dimension to concatenate along

# Inputs to the model
x1  = torch.randn(2, 5, 64, 64)
