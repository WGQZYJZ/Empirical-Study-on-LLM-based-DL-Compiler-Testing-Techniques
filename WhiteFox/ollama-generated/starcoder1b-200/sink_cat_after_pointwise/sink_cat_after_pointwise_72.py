
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 1)

    def forward(self, x1):
        v1 = torch.cat([x1, x2], dim=0)  # Concatenate tensors along a dimension
        v2 = torch.relu(torch.reshape(v1, (2 * 2,))))  # Apply pointwise unary operation to the reshaped tensor
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(4, 2, 3)
