
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1, x2):
        v1 = torch.cat([x1, x2], dim=0) # Sink tensor into the cat axis, e.g., dim=0
        v2 = v1.view(-1, 4)            # Reshape the sinked tensor (dim=0 is changed to -1).
        v3 = torch.relu(v2)             # Apply a pointwise unary operation (e.g., ReLU or Tanh) to the reshaped tensor.
        return v3


# Inputs to the model
x1 = torch.randn(4, 2, 2)
x2 = torch.randn(8, 5, 2)
