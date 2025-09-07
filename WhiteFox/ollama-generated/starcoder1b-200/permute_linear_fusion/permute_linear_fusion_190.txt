
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        t1 = x1.permute(0, 2, 1)  # Permute the input tensor
        v1 = torch.nn.functional.linear(t1, self.linear.weight, self.linear.bias)  # Apply linear transformation to the permuted tensor
        return v1


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 2)
