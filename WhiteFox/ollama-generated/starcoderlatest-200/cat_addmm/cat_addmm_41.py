
class Model(torch.nn.Module):
    def __init__(self, dim: int = 1):
        super().__init__()
        self.t2 = torch.nn.Conv2d(8, 30, 3, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = torch.addmm(x1, mat1, mat2)
        v2 = torch.cat([v1], dim)
        return v2

# Initializing the model
m = Model()


