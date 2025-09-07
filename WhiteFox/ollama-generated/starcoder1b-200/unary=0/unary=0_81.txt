
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = torch.pow(v1, 2)
        v4 = torch.pow(v3, 2)
        v5 = v4 * 0.044715
        v6 = torch.tanh(v5) + 1
        v7 = v2 * v9
        return v7


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
