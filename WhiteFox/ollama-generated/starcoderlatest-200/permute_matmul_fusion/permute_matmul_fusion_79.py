
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = torch.permute(x1, 0, 2, 1)
        v2 = torch.permute(x2, 0, 2, 1)
        return torch.bmm(v1, v2)
