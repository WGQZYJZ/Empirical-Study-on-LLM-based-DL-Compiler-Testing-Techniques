
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(...)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)  # Use the permuted output tensor of the linear transformation.
        return self.linear(v1)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 4, 4)  # No need to permute this input
