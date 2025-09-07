
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.cat([x1, x2, ...], dim=...) # Reuse the permuted tensor for `cat`. It will be used as an input for a pointwise linear function.
        return torch.relu(self.linear(v1))  # Apply a pointwise unary operation to the reshaped tensor

# Initializing the model
m = Model()


