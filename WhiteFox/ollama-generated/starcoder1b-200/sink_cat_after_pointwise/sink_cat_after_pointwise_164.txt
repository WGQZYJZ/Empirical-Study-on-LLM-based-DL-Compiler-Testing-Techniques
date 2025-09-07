
class Model(torch.nn.Module):
    def __init__(self, input_size: int):
        super().__init__()
        self.linear = torch.nn.Linear(input_size + 1, 2)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.cat([v1, v1], dim=0) # Reshape the concatenated tensor after a pointwise unary operation like ReLU or Tanh
        v3 = torch.relu(v2)   # Apply a pointwise unary operation (e.g., ReLU or Tanh) to the reshaped tensor
        return v3

# Initializing the model
m = Model(input_size=3)


