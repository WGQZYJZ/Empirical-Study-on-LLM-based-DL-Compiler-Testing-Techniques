
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.relu = torch.nn.ReLU()

    def forward(self, x1, x2, x3):
        v1 = torch.cat([x1, x2], dim=1)  # Concatenate the two input tensors along axis 1 (column wise)
        v2 = v1.view(-1, 4)           # Reshape the concatenated tensor into shape [n x m] where n is the number of elements and m is 4
        v3 = self.relu(v2)            # Apply a pointwise unary operation to reshaped tensor (e.g., ReLU or Tanh)

        return v3

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 4, 4)   # Tensor of shape [n x m] where n is the number of elements and m is 4
x2 = torch.randn(2, 2)     # Tensor of shape [m x n] where n is the number of elements and m is 2
x3 = torch.randn(2, 2)     # Tensor of shape [m x n] where n is the number of elements and m is 2
