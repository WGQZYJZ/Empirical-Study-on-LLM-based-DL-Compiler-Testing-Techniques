
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, y1):
        v1 = torch.permute(x1, 0, 2)
        v2 = torch.bmm(v1, y1)
        return v2


# Initializing the model