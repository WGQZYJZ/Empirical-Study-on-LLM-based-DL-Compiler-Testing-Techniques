
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        return torch.nn.functional.linear(v1, self.weight, self.bias)


# Inputs to the model
x1 = torch.randn(1, 4, 4)
