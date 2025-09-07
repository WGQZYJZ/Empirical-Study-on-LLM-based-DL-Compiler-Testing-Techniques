
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.relu = torch.nn.ReLU()

    def forward(self, x1, x2):
        v1 = torch.cat([x1, x2], dim=0) # Concatenate tensors along a dimension
        v2 = v1.view(2, -1) # Reshape the concatenated tensor
        v3 = self.relu(v2) # Apply a pointwise unary operation (e.g., ReLU or Tanh) to the reshaped tensor
        return v3


# Initializing the model
m = Model()
x1 = torch.randn(1, 2, 4)
x2 = torch.randn(1, 2, 4)
