
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2, ..., xn):
        t1 = torch.cat([x1, x2], dim=...)
        ...
        return out

    def output(self):
        return self.__output__

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 4)
x2 = torch.randn(1, 6)
...
x7 = torch.randn(1, 8)
out = m(x1, x2, ..., x7)

