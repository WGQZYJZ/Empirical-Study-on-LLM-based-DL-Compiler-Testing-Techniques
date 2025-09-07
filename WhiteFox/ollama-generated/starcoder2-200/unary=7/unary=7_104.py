
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64, 32)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 * clamp(min=0, max=6, l1 + 3)
        v3 = v2 / 6 
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(5748, 64) # Input tensor of size (N,D): N data points each with D features

