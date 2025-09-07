
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, t1, t2):  # Two tensors
        v3 = torch.cat([t1, t2], dim=0)  # Concatenate the two tensors along a dimension
        v4 = v3.view(-1, 4*5)            # Reshape the concatenated tensor to a new shape (-1 means infer from size)
        v5 = torch.relu(v4)              # Apply a pointwise unary operation (e.g., ReLU or Tanh) to the reshaped tensor
        return v5


# Initializing the model
m  = Model()

# Inputs to the model
t1 = torch.randn(2, 3)
t2 = torch.randn(4, 6)
