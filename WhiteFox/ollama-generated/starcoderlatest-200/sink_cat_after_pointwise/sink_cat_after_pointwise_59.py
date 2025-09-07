
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.cat([x1, x1], dim=1)
        v2 = v1.view(-1, 4)
        v3 = torch.relu(v2)
        return self.linear(v3)


# Input to the model
__input__ = torch.randn(1, 2, 2)
