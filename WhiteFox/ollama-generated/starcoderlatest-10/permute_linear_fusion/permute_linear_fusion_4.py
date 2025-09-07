
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.ones_like(x1)
        t2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        return t2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(2, 3, 4)
