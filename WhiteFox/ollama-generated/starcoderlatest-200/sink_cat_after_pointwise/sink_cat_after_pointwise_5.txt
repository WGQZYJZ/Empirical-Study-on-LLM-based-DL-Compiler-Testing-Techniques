
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1, x2):
        v1 = torch.cat([x1, x2], dim=0)  # Concatenate two tensors along dimension 0
        v2 = v1.view(-1, 4)           # Reshape the concatenated tensor
        v3 = torch.relu(v2)           # Apply a pointwise unary operation (e.g., ReLU or Tanh) to the reshaped tensor
        return v3
# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(5, 2, 2)
x2 = torch.randn(5, 2, 2)
