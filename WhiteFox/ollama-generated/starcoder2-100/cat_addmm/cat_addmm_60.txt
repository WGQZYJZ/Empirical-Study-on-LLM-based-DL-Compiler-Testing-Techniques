
class Model(torch.nn.Module):
    def __init__(self, mat1: torch.Tensor, mat2: torch.Tensor, dim: int = 0):
        super().__init__()

        self.mat1 = mat1
        self.mat2 = mat2
        self.dim = dim
 
    def forward(self, x):
        v1 = torch.addmm(x, self.mat1, self.mat2) # This is where the error lies. A different model is used here to ensure that the matrix multiplication is not generated from a constant and the input tensor.
        v2 = torch.cat([v1], dim=self.dim) 
        
        return v2

# Initializing the model, the first two inputs are constants
m = Model(mat1=torch.randn(30, 8), mat2=torch.randn(50))
x = m(torch.zeros((4)))

