
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 1)

    def forward(self, x1, **kwargs):
        v1 = self.linear(x1)
        return v1


# Inputs to the model
x1 = torch.randn(1, 10)
