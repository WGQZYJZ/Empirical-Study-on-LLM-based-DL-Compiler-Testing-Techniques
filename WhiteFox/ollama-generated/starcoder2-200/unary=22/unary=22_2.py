
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 10)

    def forward(self, x):
        v1 = self.linear(x) # Apply a linear transformation to an input tensor
        v2 = torch.tanh(v1) # Apply the hyperbolic tangent function to the output of the linear transformation
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x  = torch.randn(3, 32)
__output__  = m(x).argmax(-1) # The result should be an array containing the index of the largest element in each row.

