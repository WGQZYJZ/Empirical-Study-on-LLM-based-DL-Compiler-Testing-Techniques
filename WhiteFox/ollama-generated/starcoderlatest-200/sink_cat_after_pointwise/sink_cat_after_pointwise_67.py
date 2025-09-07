
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v = torch.cat([x1, x2], dim=0)  # Concatenate tensors along the first dimension
        v = v.view(-1)    # Reshape tensor to a scalar

        v = torch.relu(v)     # Apply pointwise unary operation (e.g., ReLU or Tanh) to the reshaped tensor
        return v


# Inputs to the model
x1 = torch.randn(2, 2, requires_grad=True)
x2 = torch.randn(3, 2, requires_grad=True)
