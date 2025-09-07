
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        t1 = torch.cat([x1, x2], dim=...) # Re-order input with respect to time dimension
        t2 = t1.view(...)  # Reshape the concatenated tensor
        t3 = torch.relu(t2) # Apply a pointwise unary operation (e.g., ReLU or Tanh) to the reshaped tensor
        return t3


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(2, 2, 4)  # Tensor with shape [2, 4]
x2  = torch.randn(4, 4)        # Tensor with shape [4, 4]
