
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.cat([v1, v1], dim=-1).view(2, -1).permute(0, 2, 1)
        v3 = torch.relu(t2)
        return v3


# Initializing the model
m = Model()
__input__ = x1
