
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
        self.addmm = torch.nn.Parameter(torch.zeros((4, 7)))
 
    def forward(self, x1):
        v1  = torch.addmm(x1, mat1, mat2)
        v2  = torch.cat([v1], dim)
        return v6

# Initializing the model
m  = Model()

# Inputs to the model
mat1  = torch.randn(4, 7) # A randomly generated matrix of size 4x7
mat2  = torch.randn(8, 9) # A randomly generated matrix of size 8x9
input = torch.randn(3, 64, 64) # Input to the model of size 1x3x64x64
 
__output__  = m(input)

