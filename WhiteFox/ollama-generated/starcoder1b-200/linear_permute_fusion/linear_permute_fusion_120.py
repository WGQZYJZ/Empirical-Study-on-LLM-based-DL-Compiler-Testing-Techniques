
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1, 3)

    def forward(self, x):
        v = x + 5  # input+bias
        return torch.nn.functional.linear(v, self.linear.weight, self.linear.bias)


# Inputs to the model
x = torch.randn(2, 1, 3, 4)
