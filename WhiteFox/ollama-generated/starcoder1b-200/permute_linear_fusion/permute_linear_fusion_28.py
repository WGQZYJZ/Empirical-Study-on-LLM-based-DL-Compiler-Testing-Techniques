
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        return torch.softmax(self.linear(x1), dim=1)


# Inputs to the model
x1 = torch.randn(1, 2, 2)
