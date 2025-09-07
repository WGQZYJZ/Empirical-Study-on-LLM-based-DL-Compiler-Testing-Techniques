
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, mat1, mat2):
        v1 = torch.addmm(x1, mat1, mat2)
        return torch.cat([v1], 0)


# Initializing the model