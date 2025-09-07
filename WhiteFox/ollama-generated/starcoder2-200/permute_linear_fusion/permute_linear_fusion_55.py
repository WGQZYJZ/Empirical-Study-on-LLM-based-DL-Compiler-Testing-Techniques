
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 1)

    def forward(self, x1):
        v1 = torch.ones(2, 3) * x1 # Use the input tensor as the main input for the linear function without applying the permute method.
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        return v2


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(3) # The shape of the input tensor is (3,) instead of (3,).
__output__= m(x1)