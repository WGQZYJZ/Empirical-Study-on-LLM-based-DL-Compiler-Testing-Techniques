
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        return torch.nn.functional.linear(x1, self.weight, self.bias)


# Inputs to the model
x1 = torch.randn(3, 2, 3)
