
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = torch.cat([x1, x2], dim=-1)  # Concatenate tensors along a dimension
        v2 = v1.view(-1, 2)  # Reshape the concatenated tensor
        v3 = torch.relu(v2)  # Apply a pointwise unary operation (e.g., ReLU or Tanh) to the reshaped tensor
        return v3


# Initializing the model
m = Model()
# Inputs to the model
x1 = torch.randn(1, 4, 10)
x2 = torch.randn(1, 5, 20)
