
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32 * 16, 8)
 
    def forward(self, x1, other):
        v1 = self.conv(x1)
        v2 = v1 + other
        return v6


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 32, 16, 48)
other = torch.randn(32 * 16)
