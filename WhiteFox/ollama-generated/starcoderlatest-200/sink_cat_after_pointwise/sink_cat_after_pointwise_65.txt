
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 3)

    def forward(self, x1):
        v1 = torch.cat([x1, x1], dim=0) # Concatenate input tensor and itself on dimension zero (along the first axis). The concatenation order is preserved during the computation.
        v2 = v1.view(v1.shape[0] * v1.shape[1], -1) # Reshape to one-dimensional array, where rows are all copied from input tensors into a single row.
        v3 = torch.relu(v2) # Apply the pointwise unary operation (e.g., ReLU or Tanh) to the reshaped tensor.
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 2)
