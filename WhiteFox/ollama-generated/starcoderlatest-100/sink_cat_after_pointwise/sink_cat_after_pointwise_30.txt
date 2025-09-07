
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1, x2):
        v1 = torch.cat([x1, x2], dim=0)
        v2 = v1.view(-1, v1.size(-1))
        return self.linear(v2)


# Inputs to the model
x1 = torch.randn(5, 2, 2)
x2 = torch.randn(5, 3, 2)
