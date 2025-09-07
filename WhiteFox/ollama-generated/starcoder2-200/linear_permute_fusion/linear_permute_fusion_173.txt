
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v3 = torch.nn.functional.linear(x1, self.linear.weight, bias=None) # Apply linear transformation without the bias term in linear function
        v4 = v3.permute(0, 2, 1)
        return v4


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(5, 2, 2) # Input tensors can have any dimensionality.
__output__  = m(x1)
