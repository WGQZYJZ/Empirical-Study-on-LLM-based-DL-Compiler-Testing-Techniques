
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v = torch.nn.functional.linear(x1)
        v  = v.permute()

        return v


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(2, 3)
__output__  = m(x1)


