
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.relu = torch.nn.ReLU()

    def forward(self, x1):
        v1 = torch.cat([x1, 2 * x1], dim=1)  # Concatenate tensors along a dimension
        v2 = v1.view(v1.shape[0], -1)   # Reshape the concatenated tensor
        v3 = self.relu(v2)             # Apply a pointwise unary operation (e.g., ReLU or Tanh) to the reshaped tensor
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 2)
