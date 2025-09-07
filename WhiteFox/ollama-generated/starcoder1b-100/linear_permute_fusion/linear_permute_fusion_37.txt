
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 5)

    def forward(self, x):
        v = x.view(-1, 784)
        v = self.linear(v)
        return v


# Inputs to the model
x1 = torch.randn(2, 784)
