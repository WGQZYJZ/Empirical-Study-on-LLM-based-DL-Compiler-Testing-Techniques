
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.cat([x1, x2], dim=0)  # Concatenate tensors along dimension 0
        v2 = v1.view(-1, 8)  # Reshape the concatenated tensor
        v3 = torch.relu(v2)  # Apply a pointwise unary operation (e.g., ReLU or Tanh) to the reshaped tensor
        return v3


# Inputs to the model
x1 = torch.randn(2, 8)
x2 = torch.randn(4, 8)
