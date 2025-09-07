
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v = torch.cat([x1, x2], dim=0) # Concatenate tensor along dimension 0
        u = torch.relu(v).view(-1, 4, 4)  # Reshape the concatenated tensor and apply pointwise unary operation (e.g., ReLU or Tanh)
        return u


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 3)
x2 = torch.randn(1, 4, 4)
