
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        t1 = torch.cat([x1, 2 * x1], dim=1)
        t2 = t1.view(-1, 4, 2) # Reshape the concatenated tensor
        t3 = torch.relu(t2) # Apply a pointwise unary operation (e.g., ReLU or Tanh) to the reshaped tensor
        return t3

# Initializing the model
m = Model()
x1 = torch.randn(1, 64)
