
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Linear(3, 4)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 - other
        v3 = torch.relu(v2)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
other = 0.5 * (torch.randn(1, 8)) # Generate a random value for other
x1 = torch.randn(1, 3, 64, 64)
