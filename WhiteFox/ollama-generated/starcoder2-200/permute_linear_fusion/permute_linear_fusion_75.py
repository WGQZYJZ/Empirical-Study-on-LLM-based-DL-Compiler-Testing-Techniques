
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = x1.permute(0, 3, 1).reshape(-1, 4) # Shape [2] -> [-1], then add a new dimension to the front of it. It is equivalent to the permute method but with fewer parameters.
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)

        return v2


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(1, 3, 4, 5)
__output__  = m(x1)


