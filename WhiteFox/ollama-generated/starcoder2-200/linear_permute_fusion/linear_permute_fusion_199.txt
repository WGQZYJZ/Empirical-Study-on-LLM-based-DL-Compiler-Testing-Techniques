
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, self.linear.weight)
        v2  = v1.permute(...) # This is a new pattern
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(50, 4096)
__output__  = m(x1)