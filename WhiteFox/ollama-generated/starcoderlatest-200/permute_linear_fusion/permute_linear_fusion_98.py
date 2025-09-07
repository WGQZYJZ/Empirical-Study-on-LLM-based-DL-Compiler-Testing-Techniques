
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 1)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1) # Modify the shape of the input tensor, swap the last two dimensions
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias) # Apply linear transformation to the permuted tensor.
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 2, 2)
