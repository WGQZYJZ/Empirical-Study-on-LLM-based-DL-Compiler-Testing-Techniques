
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5
        return output


# Initializing the model
m = Model()


# Inputs to the model
query  = torch.randn(4, 7, 7, 3)
key    = torch.randn(4, 7, 7, 8)
scale_factor = 0.5
