
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 1)

    def forward(self, x1, x2):
        v1 = torch.cat([x1, x2], dim=0)  # Concatenate the input tensors in a dimension with 'dim' set to zero
        v2 = v1.view(-1, 4)  # Reshape the concatenated tensor
        v3 = torch.relu(v2)  # Apply a pointwise unary operation (e.g., ReLU or Tanh) to the reshaped tensor
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 2, requires_grad=True)
x2 = torch.randn(2, 2, requires_grad=True)
