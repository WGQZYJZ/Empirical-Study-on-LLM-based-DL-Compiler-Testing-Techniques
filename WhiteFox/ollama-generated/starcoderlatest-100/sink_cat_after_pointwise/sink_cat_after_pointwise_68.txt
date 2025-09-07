
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.relu = torch.nn.ReLU()

    def forward(self, t1, t2):
        v1 = torch.cat([t1, t2], dim=0) # Concatenate two tensors along the first dimension
        v2 = v1.view(-1)            # Reshape concatenated tensor into a vector
        v3 = self.relu(v2)          # Apply pointwise unary operation (ReLU) to the reshaped tensor
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(10, 2)
x2 = torch.randn(5, 2)
