
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.cat([v1, v1], dim=-1)
        v3 = torch.relu(v2)  # Apply a pointwise unary operation (e.g., ReLU or Tanh) to the reshaped tensor
        return v3


# Initializing the model
m = Model()


