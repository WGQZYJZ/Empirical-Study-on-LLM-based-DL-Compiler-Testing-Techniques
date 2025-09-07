
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 2)

    def forward(self, x1, x2):
        t1  = torch.cat([x1, x2], dim=1) # Concatenate two tensors along the third dimension.
        t2  = t1.view(1, -1)         # Reshape tensor to a vector along the second dimension.
        t3  = torch.relu(t2)       # Apply pointwise unary operation (e.g., ReLU or Tanh) on this vector.
        return t3


# Initializing the model
m = Model()

# Inputs to the model
x1, x2 = torch.randn(2, 2), torch.randn(2, 2)
