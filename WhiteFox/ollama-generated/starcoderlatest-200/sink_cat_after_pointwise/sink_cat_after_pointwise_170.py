
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2, x3):
        # Concatenate input tensors along a dimension
        v1 = torch.cat([x1, x2, x3], dim=1)

        # Reshape the concatenated tensor
        v2 = v1.view(-1)

        # Apply a pointwise unary operation (e.g., ReLU or Tanh) to the reshaped tensor
        # and return the result
        t1 = torch.relu(v2)
        return t1


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 3, requires_grad=True)
x2 = torch.randn(4, 3, requires_grad=True)
x3 = torch.randn(4, 3, requires_grad=True)
