
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.relu = torch.nn.ReLU()

    def forward(self, x1):
        v1 = torch.cat([x1, x2], dim=1)  # Concatenate two tensors along a dimension
        v2 = v1.view(-1)         # Reshape the concatenated tensor into vector
        v3 = self.relu(v2)        # Apply a pointwise unary operation to the reshaped tensor
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(5, 2)
x2 = torch.randn(3, 2)
