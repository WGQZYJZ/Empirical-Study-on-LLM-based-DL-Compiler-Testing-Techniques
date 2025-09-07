
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(x1, x2, x3):
        v = torch.cat([x1, x2, x3], dim=0) # Concatenate tensors along a dimension
        v  = v.view(-1) # Reshape the concatenated tensor
        v  = torch.relu(v) # Apply a pointwise unary operation (e.g., ReLU or Tanh) to the reshaped tensor
        return v


# Initializing the model
m = Model()
# Inputs to the model
x1 = torch.randn(2, 3, requires_grad=True)
x2 = torch.randn(3, 4, requires_grad=True)
x3 = torch.randn(5, 6, requires_grad=True)
