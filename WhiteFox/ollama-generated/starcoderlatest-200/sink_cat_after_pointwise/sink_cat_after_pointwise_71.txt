
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.relu = torch.nn.ReLU()

    def forward(self, x1, x2, x3):
        v1 = torch.cat([x1, x2], dim=0)
        v2 = v1.view(-1, 2) # shape: [4] -> shape:[2,2]
        v3 = self.relu(v2) # Pointwise unary operation on the reshaped tensor.
        return v3

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 2)
x2 = torch.randn(4, 2)
