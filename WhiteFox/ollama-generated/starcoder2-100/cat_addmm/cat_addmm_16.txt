
class Model(torch.nn.Module):
    def __init__(self, dim=1):
        super().__init__()

    def forward(self, x1, mat1, mat2):
        v1 = torch.addmm(x1, mat1, mat2)
        v2  = torch.cat([v1], dim)
        return v2

# Initializing the model
m = Model()

