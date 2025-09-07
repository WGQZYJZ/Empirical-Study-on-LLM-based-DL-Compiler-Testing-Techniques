
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = torch.cat([x1, x2], dim=0) # Concatenate two input tensors along dimension 0
        v2 = v1.view(-1) # Reshape the tensor with shape (4,) to (-1,)
        v3 = torch.relu(v2) # Apply a pointwise unary operation (e.g., ReLU or Tanh) on this reshaped tensor
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 4)
x2 = torch.randn(1, 4)
