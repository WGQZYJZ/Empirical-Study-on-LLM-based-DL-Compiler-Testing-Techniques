
class Model(torch.nn.Module):
    def __init__(self, inplace=False):
        super().__init__()
        self.linear = torch.nn.Linear(10, 10)

    def forward(self, x):
        v1 = self.linear(x)
        return torch.cat([v1, v1], dim=-1)


