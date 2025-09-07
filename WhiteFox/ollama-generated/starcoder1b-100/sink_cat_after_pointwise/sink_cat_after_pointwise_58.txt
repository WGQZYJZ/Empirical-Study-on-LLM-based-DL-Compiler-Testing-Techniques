
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 3)

    def forward(self, x1):
        v1 = x1[:, 0:2]
        v2 = self.linear(v1)
        return v2


# Inputs to the model
x1 = torch.randn(3, 2)
