
class Model(torch.nn.Module):
    def __init__(self, dim=1024):
        super().__init__()
        self.dense = torch.nn.Linear(3 * 64 ** 2 + 3, dim)
 
    def forward(self, x1):
        v1 = torch.addmm(x1, mat1, mat2)
        v2 = torch.cat([v1], dim)
        return v2

# Initializing the model