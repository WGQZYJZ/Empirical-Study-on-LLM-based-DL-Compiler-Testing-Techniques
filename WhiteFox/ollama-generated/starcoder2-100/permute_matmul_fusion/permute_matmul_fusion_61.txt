
class Model(torch.nn.Module):
    def __init__(self, dim1):
        super().__init__()
        self.linear = torch.nn.Linear(dim1, 2)

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1)
        v3 = torch.bmm(v1, x2)
        return v3


# Initializing the model