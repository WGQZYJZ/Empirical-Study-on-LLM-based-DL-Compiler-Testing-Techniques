
class Model(torch.nn.Module):
    def __init__(self, num_inputs, dim):
        super().__init__()
        self.conv = torch.nn.Conv2d(num_inputs, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.cat([v1], dim)
        return v2

# Initializing the model
m = Model(3, 10)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
