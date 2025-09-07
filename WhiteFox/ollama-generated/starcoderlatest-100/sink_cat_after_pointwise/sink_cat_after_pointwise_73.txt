
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 1)

    def forward(self, x1, x2):
        v1 = torch.cat([x1, x2], dim=0) # Concatenate two input tensors along the zeroth dimension.
        v2 = v1.view(-1, 4) # Reshape the concatenated tensor into a vector with shape [2, 4]
        v3 = torch.nn.functional.relu(v2) # Apply a pointwise unary operation (e.g., ReLU or Tanh) to the reshaped tensor
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 2) # Tensor of shape [1, 2]
x2 = torch.randn(1, 2) # Tensor of shape [1, 2]
