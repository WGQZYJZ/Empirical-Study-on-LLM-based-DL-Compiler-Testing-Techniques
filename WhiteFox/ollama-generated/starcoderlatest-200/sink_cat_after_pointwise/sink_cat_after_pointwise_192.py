
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2, ..., xn):
        v  = torch.cat([x1, x2, ...], dim=1) # Concatenate tensors along a dimension
        v1 = v.view(...)     # Reshape the concatenated tensor
        v2 = torch.relu(v1) # Apply a pointwise unary operation (e.g., ReLU or Tanh) to the reshaped tensor
        return v2

# Inputs to the model
x1, x2, ...xn = torch.randn(1, 2, 2)
