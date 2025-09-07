
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 3)

    def forward(self, x1):
        v1 = torch.cat([x1, x2], dim=0) # Concatenate two input tensors along dimension 0
        v2 = torch.cat([v1, v1.permute(0, 2, 1)], dim=-1) # Concatenate the first two of the concatenated tensor with reversed permutation along -1 axis
        v3 = torch.relu(v2) # Apply a pointwise unary operation (e.g., ReLU or Tanh) to the reshaped tensor
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 3)
x2 = torch.randn(1, 4, 5)
