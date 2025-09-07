
class Model(torch.nn.Module):
    def __init__(self, dim=0):
        super().__init__()
        self.addmm = torch.nn.AddMM()
 
    def forward(self, x1, mat1, mat2):
        v1 = self.addmm(x1, mat1, mat2)
        v2 = torch.cat([v1], dim)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(256)
mat1 = torch.randn(256, 256)
mat2 = torch.randn(256, 256)
