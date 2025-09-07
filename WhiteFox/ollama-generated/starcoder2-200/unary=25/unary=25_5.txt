
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.where(v1 > 0., v1, v1 * negative_slope)
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(10000, 3)
negative_slope = torch.ones(1).fill_(0.5) # The value for the negative slope is set to 0.5
__output__  = m(x1, negative_slope)

