
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        t1 = torch.cat([x1, x2], dim=0) # Concatenate two input tensors along the dimension 0
        t2 = t1.view(-1)   # Reshape the concatenated tensor to a vector
        t3 = torch.relu(t2) # Apply a pointwise unary operation (e.g., ReLU or Tanh) on the reshaped tensor
        return t3

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 10)
x2 = torch.randn(4, 5)
