
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.cat([v1, v1], dim=1).view(-1, 4).t()  # Concatenate tensors along a dimension
        v3 = torch.relu(torch.matmul(v2, self.linear.weight), True) # Apply a pointwise unary operation (e.g., ReLU or Tanh) to the reshaped tensor
        return v3


# Initializing the model
m = Model()
x1 = torch.randn(1, 4, 2)
