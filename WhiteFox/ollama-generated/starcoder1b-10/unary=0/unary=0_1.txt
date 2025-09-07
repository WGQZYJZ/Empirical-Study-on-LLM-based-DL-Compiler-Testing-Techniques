
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1) * 0.5
        v2 = torch.sqrt(v1)
        v3 = v2  # Squared
        v4 = v3 * v1  # Cubed
        v5 = torch.exp(v4)  # Exponential
        v6 = v1 + v5  # Add
        v7 = v6 * 0.7978845608028654  # Multiply
        v8 = torch.tanh(v7)  # Hyperbolic tangent
        v9 = v8 + 1  # Add
        v10 = v2 * v9  # Multiply
        return v10


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
