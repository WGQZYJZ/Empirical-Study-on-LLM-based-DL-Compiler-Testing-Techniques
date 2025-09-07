
class Model(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
 
    def forward(self, x1, m1, m2, x4):
        v1  = torch.addmm(x1, m1, m2) 
        return torch.cat([v1], dim=dim), x4


# Initializing the model
m  = Model(0)

# Inputs to the model
mat1 = torch.randn(8,3,56,56)
mat2 = torch.randn(8,9,56,56)
x1   = torch.randn(7,4,56,56)
dim  = 0 # Concatenate the result along axis=dim


# Outputs from the model
__output__  = m(x1, mat1, mat2, x1)