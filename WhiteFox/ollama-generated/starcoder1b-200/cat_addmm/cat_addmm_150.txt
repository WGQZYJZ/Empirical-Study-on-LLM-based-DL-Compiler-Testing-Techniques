
class Model(torch.nn.Module):
    def __init__(self, mat1=None, mat2=None, dim=-1):
        super().__init__()
        self.mat1 = mat1
        self.mat2 = mat2
        self.dim  = dim

    def forward(self, x1):
        # Compute the matrix multiplication of mat1 and mat2 (tensor) and concatenate it to an input tensor (tensor).
        t1 = torch.addmm(x1, self.mat1, self.mat2) 
        # Perform a concatenation operation in the specified dimension with `t1`.
        t2 = torch.cat([t1], dim=self.dim)  # Concatenate the result along `dim` (dimension of the input tensor).
        return t2


# Initializing the model
m = Model(torch.randn(4, 3), torch.randn(4, 2))
