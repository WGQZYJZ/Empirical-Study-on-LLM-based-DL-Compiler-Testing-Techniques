
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, inp=None):
        v2 = torch.mm(x1) + 1
        return v5

