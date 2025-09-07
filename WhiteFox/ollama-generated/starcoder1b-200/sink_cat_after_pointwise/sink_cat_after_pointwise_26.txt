
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 3)
        self.linear2 = torch.nn.Linear(3, 4)

    def forward(self, x1, x2=None):
        if x2 is None:
            v1 = x1.permute(0, 2, 1)  # Permute the input tensor
            v2 = self.linear1(v1)       # Apply linear transformation to the permuted tensor
            v3 = self.linear2(v2)       # Apply a pointwise unary operation (e.g., ReLU or Tanh) to the permuted tensor
            return v3
        else:
            v1  = x1.permute(0, 2, 1)      # Permute the input tensor
            v2  = self.linear1(v1)       # Apply linear transformation to the permuted tensor
            v3  = self.linear2(v2)       # Apply a pointwise unary operation (e.g., ReLU or Tanh) to the permuted tensor
            return torch.cat([v1, x2], dim=1), v3


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(1, 2, 2) # [batch_size, feature_dimension]
x2  = None  # Can also be None
