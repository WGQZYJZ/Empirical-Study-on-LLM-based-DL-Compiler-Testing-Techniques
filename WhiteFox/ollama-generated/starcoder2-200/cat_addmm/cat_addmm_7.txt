
class Model(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.mat1  = torch.ones([248, 39], dtype=torch.float32) / 5678
        self.mat2  = torch.zeros((40, 4), dtype=torch.float32)
 
    def forward(self, x):
         v1  = x 
         v2  = torch.addmm(v1, mat1, mat2)
         v3  = torch.cat([v2], dim)
         return v3

# Initializing the model
m  = Model()
dim  = 4

 # Inputs to the model
x   = torch.randn(256, 80).float()
__output__  = m(x)