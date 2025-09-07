
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = v2 + v2 - v2  # Replacement of v4 = torch.pow(v3, 3) with v3 * t3
        v4 = v3 * 0.7978845608028654 
        v5 = v1 * v4 + v4 - v4   # Replacement of v5 = torch.tanh(v4) with torch.tanh(t7), t7 = t7 * t7
        return v3


# Initializing the model
m = Model()

# Inputs to the model