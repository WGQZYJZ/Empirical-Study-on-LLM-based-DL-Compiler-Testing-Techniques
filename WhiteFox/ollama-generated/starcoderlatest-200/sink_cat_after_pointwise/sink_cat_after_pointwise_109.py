
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 5)
        self.linear2 = torch.nn.Linear(5, 3)

    def forward(self, x1, x2):
        v1 = torch.cat([x1, x2], dim=1)  # Concatenate x1 and x2 along dimension 1
        v2 = v1.view(v1.size(0), -1)  # Reshape to a vector
        v3 = torch.relu(self.linear2(v2))  # Apply a pointwise unary operation (e.g., ReLU or Tanh) to the reshaped tensor
        return self.linear1(v3)


# Initializing the model
m = Model()

x1 = torch.randn(1, 2, 5)
x2 = torch.randn(1, 8, 5)
