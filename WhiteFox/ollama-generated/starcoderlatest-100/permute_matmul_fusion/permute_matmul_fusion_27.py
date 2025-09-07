
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1, x2=None):
        if x2 is None:
            v1 = x1.permute(0, 2, 1)
        else:
            v1 = torch.bmm(x1, x2)
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        return v2

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 2, 2)
__output_A__ = m(x1)

x2 = torch.randn(1, 2, 3)
__output_B__ = m(x1, x2=x2)


