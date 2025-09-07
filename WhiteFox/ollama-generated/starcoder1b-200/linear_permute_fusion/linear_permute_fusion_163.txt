
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1, 3)

    def forward(self, x1):
        v1 = torch.zeros(1, 2, 2).normal_(0, 0.25)
        v2 = self.linear(x1)
        return v2


# Inputs to the model
x1 = torch.randn(3, 2, 4)
