
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.permute(x1, (0, 3, 1))
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(30, 5, 6, 7)
__output__  = m(x1)
