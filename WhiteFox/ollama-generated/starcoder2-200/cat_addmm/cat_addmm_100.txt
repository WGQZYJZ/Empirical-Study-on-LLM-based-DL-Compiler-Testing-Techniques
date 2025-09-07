
class Model(torch.nn.Module):
    def __init__(self, dim=1):
        super().__init__()
        self.dim  = dim

    def forward(self, x1):
        v1  = torch.addmm(x1, mat1, mat2) 
        v2  = torch.cat([v1], dim=self.dim)
        return v2

# Initializing the model
m  = Model()
input = torch.randn(50, 384, 32, 32)
__output__  = m(input)

