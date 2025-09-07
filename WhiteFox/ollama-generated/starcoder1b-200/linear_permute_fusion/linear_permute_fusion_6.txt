
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        t = torch.nn.functional.linear(x1, self.weight, self.bias)
        t2 = t.permute(..., 1, 0) # Permute the output tensor from the linear transformation.
        return t2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 2, 2)
