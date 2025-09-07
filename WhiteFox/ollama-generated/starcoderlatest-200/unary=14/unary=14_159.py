
class GLUModel(torch.nn.Module):
    def __init__(self, num_features):
        super().__init__()
        self.conv = torch.nn.Conv2d(num_features * 3, num_features, 1)
 
    def forward(self, x1):
        t1 = self.conv(x1)
        t2 = torch.sigmoid(t1)
        t3 = t1 * t2
        return t3

# Initializing the model
m = GLUModel(num_features=3)

# Inputs to the model
x1 = torch.randn(1, 8, 64, 64)
