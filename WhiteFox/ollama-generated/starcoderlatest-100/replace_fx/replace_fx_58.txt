
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 3)

    def forward(self, x1):
        v1 = torch.rand_like(x1, ...)  # Generate a tensor with the same size as input_tensor filled with random numbers
        v2 = torch.nn.functional.dropout(v1, ...)  # Apply dropout to the tensor
        v3 = self.linear(v2) # Perform linear transformation on tensor generated in previous step
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(2, 4, 5)
