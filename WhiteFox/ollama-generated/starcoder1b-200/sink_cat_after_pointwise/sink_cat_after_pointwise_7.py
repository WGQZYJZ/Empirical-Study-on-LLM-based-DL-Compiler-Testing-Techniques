
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.cat([x1, x1, ...], dim=0)
        v2 = torch.relu(v1)  # Apply a pointwise unary operation (e.g., ReLU or Tanh) to the reshaped tensor
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(4, 5, 3)
