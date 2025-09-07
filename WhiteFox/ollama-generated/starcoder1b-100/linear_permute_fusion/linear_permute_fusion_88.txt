
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 2)

    def forward(self, x1):
        v1 = torch.stack((x1[:, :, 0], x1[:, :, 1]), dim=-1)
        v2 = self.linear(v1)
        return v2


# Inputs to the model
x1 = torch.randn(3, 10, 5, 2)
