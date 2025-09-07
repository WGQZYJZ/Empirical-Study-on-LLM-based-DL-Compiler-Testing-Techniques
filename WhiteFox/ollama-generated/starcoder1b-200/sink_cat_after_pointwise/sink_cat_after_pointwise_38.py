
class Model(torch.nn.Module):
    def __init__(self, dim: int = 3):
        super().__init__()
        self.linear = torch.nn.Linear(dim, 2)

    def forward(self, x1, x2):
        v1 = torch.cat([x1, x2], -1)  # Concatenate both tensors along the -1 dimension
        v2 = torch.relu(v1)  # Apply a pointwise unary operation (like ReLU or Tanh) to both tensors
        return v2


# Initializing the model
m = Model()
