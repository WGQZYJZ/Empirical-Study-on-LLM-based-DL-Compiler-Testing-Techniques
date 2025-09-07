
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v = self.linear(x1)
        return torch.nn.functional.linear(v, self.linear.weight, self.linear.bias)

# Inputs to the model
x1 = torch.randn(2, 2)
