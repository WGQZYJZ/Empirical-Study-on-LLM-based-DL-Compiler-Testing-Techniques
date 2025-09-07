
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        t1 = torch.cat([x1, x2], dim=-1)  # Concatenate tensors along a dimension
        t2 = t1.view(-1, 3)  # Reshape the concatenated tensor
        t3 = torch.relu(t2)  # Apply a pointwise unary operation (e.g., ReLU or Tanh) to the reshaped tensor
        return t3


# Initializing the model
m = Model()
x1 = torch.randn(2, 1)
x2 = torch.randn(1, 3)
