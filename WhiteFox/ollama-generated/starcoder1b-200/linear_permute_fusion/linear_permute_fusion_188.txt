
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1  = torch.nn.functional.linear(x1, ...)  # Apply linear transformation to the input tensor.
        v2  = torch.nn.functional.linear(v1, self.linear.weight, ...)  # Apply linear transformation to the permuted output tensor.
        return v2


# Initializing the model
m = Model()
x1 = torch.randn(1, 2, 2)
