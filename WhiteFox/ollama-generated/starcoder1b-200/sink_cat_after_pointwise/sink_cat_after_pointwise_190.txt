
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = x1 + x1  # Concatenate two tensors along a dimension (dim=0)
        v2 = v1.view(-1, 4)  # Reshape the concatenated tensor to fit its shape (size: -1)
        v3 = torch.relu(v2)   # Apply a pointwise unary operation (e.g., ReLU or Tanh) to the reshaped tensor
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(2, 4)  # A concatenation of two tensors that have shapes: (2, 4).
