
class Model(torch.nn.Module):
    def __init__(self, mat1, mat2, dim=0):
        super().__init__()
        self.mat1 = mat1
        self.mat2 = mat2
 
    def forward(self, x1):
        v1  = torch.addmm(x1, self.mat1, self.mat2)
        v2  = torch.cat([v1], dim=0) 
        return v2

# Initializing the model
mat1 = torch.randn(8, 3, 64, 64)
mat2 = torch.randn(7, 8, 64, 64)
 
m  = Model(mat1, mat2)
__output__  = m(torch.randn(10, 3, 64, 64))

