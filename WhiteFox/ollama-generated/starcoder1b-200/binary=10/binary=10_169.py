
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 2)

    def forward(self, x1, other):
        v1 = self.linear(x1) + other  # Apply a linear transformation to the input tensor
        return v1


# Initializing the model
m = Model()


# Inputs to the model
input_tensor = torch.randn(2, 10)  # First two inputs of the model are zero and two more inputs of the model are random numbers
