
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 1)

    def forward(self, x1, x2):
        v1 = x1 + x2  # Concatenate two inputs together.
        return self.linear(v1)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 1, 2)  # This input has one dimension, and it is the second of dimenstions in the reshape of v1.
x2 = torch.randn(1, 2, 2)  # This input also has two dimensions, but is not reshaped yet.
