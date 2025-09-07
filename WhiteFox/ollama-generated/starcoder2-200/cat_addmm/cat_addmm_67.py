
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        mat2 = torch.randn(4096)
        mat3 = torch.randn(8756, 4096)
        v1  = torch.addmm(x1, mat3, mat2)
 
        return torch.cat([v1], dim=None)


# Initializing the model