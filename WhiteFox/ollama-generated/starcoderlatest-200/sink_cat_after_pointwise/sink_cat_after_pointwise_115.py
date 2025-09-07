
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.relu = torch.nn.ReLU()

    def forward(self, x1, x2, x3, x4):
        t1 = torch.cat([x1, x2], dim=0) # Concatenate tensors along dimension 0
        t2 = t1.view(-1)            # Reshape the concatenated tensor
        t3 = torch.relu(t2)        # Apply a pointwise unary operation (e.g., ReLU or Tanh) to the reshaped tensor
        return t3


# Initializing the model
m = Model()
# Inputs to the model
x1 = torch.randn(1, 2, 4)
x2 = torch.randn(1, 2, 4)
x3 = torch.randn(1, 2, 4)
x4 = torch.randn(1, 2, 4)
