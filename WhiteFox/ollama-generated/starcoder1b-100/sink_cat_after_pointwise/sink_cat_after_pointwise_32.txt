
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.cat([x1, x1], dim=0)  # Reshape tensor1 to 3*2=6
        v2 = torch.relu(torch.unsqueeze(v1, 0))  # Apply a pointwise unary operation (e.g., ReLU or Tanh) to the reshaped tensor1
        return v2


# Inputs to the model
x1 = torch.randn(3, 2)
