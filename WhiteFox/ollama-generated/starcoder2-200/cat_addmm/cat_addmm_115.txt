

class Model(torch.nn.Module):
    def __init__(self, mat1 = None, mat2 = None, dim=0):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
 
        return v1


m  = Model()

# Initializing the model with two randomly generated matrices and a constant dimension: dim
mat1 = torch.rand(32, 54, 780, 990)
mat2 = torch.randn(63, 54, 780, 990)
dim  = 0
m  = Model(mat1= mat1, mat2=mat2, dim= dim )

 # Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
