
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, y1):
        v3  = torch.relu(torch.cat([x1 + y1], dim=0))
        return v3

