
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1, 1)

    def forward(self, x1, x2):
        v1 = torch.cat([x1, x2], dim=0)  # Concatenate input tensors along the first dimension
        v2 = v1.view(-1)  # Reshape the concatenated tensor
        v3 = torch.nn.functional.relu(v2)  # Apply a pointwise unary operation to reshaped tensor.
        return self.linear(v3)


# Initializing the model
m = Model()
x1 = torch.randn(1, 5)
x2 = torch.randn(1, 6)
