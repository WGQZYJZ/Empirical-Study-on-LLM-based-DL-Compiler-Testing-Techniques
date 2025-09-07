
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.relu(x1)  # Apply a pointwise unary operation (e.g., ReLU or Tanh) to the input tensor directly without reshaping.
        return v1

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 4)

