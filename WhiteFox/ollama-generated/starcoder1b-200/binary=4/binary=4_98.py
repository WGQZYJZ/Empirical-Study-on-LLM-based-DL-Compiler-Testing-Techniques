
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 8)

    def forward(self, x1, other=None):
        v1 = self.linear(x1) + other  # Add the two tensors and return their result
        return v1


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(2, 32)
other = torch.randn(4, 8)
