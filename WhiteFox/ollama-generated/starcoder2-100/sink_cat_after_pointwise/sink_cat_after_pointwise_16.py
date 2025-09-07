
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, y2):
        t = torch.cat([x1, y2])
        return t

