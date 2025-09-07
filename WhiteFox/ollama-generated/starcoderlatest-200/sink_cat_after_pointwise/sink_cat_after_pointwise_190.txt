
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 2)
        self.linear2 = torch.nn.Linear(2, 1)

    def forward(self, x1, x2):
        v1 = torch.cat([x1, x2], dim=0) # Permute the input tensor
        v2 = v1.view(2, 3)               # Reshape the concatenated tensor
        v3 = torch.relu(v2)              # Apply a pointwise unary operation (e.g., ReLU or Tanh) to the reshaped tensor
        v4 = self.linear1(v3)           # Project the reshaped tensor into new output dimension
        return v4


# Inputs to the model
x1 = torch.randn(2, 2, 1)   # Input of size [2, 2, 1] with shape [2 x 2]
x2 = torch.randn(3, 2, 2)   # Input of size [3, 2, 2] with shape [6 x 4]
