 2:
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        t1 = torch.rand_like(x1, ...)  # Generate a tensor with the same size as input_tensor filled with random numbers
        v1 = x1 + t1
        v2 = torch.nn.functional.linear(...)  # Apply linear transformation to the permuted tensor.
        return v2
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 2)
