
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v = torch.nn.functional.linear(x1, self.weight, self.bias)
        return v.permute(0, 2, 1)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 3)
