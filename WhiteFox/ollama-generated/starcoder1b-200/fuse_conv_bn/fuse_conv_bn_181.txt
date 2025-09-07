
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2, ...):
        if 2 <= x1.ndim <= 4:
            v = x1.permute(0, 3, 1)
        else:
            v = torch.cat([x1, x2, ...], dim=3)
        return torch.nn.functional.convXd(...)(v, self.weight, self.bias, ...)


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(1, 4, 28, 28)
x2  = torch.randn(1, 4, 28, 28)
...  # You can also generate inputs of different shape if needed
