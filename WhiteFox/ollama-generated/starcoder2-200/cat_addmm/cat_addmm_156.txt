
class Model(torch.nn.Module):
    def __init__(self, dim=1):
        super().__init__()
        self.mat1 = torch.ones((240, 3)) 
        self.mat2 = torch.randn((500, 784), device="cuda")
 
    def forward(self, x):
        v1 = torch.addmm(x, self.mat1, self.mat2)
        return torch.cat([v1], dim)


# Initializing the model
m = Model()
__output__  = m(torch.randn((800, 784), device="cuda"))

