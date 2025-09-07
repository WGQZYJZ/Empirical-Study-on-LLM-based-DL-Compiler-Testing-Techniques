
class Model(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.mat1 = torch.randn(32768)
        self.mat2 = torch.randn(32768, 50)
 
    def forward(self, x):
        v1 = torch.addmm(x, mat1, mat2) # The model does a matrix multiplication between an input tensor and two matrices.
        v2 = torch.cat([v1], dim) # The result of this operation is then concatenated along the specified dimension.
        return v2


# Initializing the model