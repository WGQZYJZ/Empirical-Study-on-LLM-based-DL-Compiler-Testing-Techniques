
class Model(torch.nn.Module):
    def __init__(self, dim=0):
        super().__init__()
        self.dim  = dim
 
    def forward(self, x1, mat1, mat2):
        v1  = torch.addmm(x1, mat1, mat2) # Matrix multiplication of matrices and inputs
        v2  = torch.cat([v1], self.dim) # Concatenation along a specified dimension
        return v2

# Initializing the model with different dimensions:
m_1d  = Model()
m_2d  = Model(1)

