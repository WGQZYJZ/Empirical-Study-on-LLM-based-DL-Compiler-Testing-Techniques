
class Model(torch.nn.Module):
    def __init__(self, dim=0):
        super().__init__()

    def forward(self, x1):
        v = torch.addmm(x1, mat1, mat2) 
        return torch.cat([v], dim)

