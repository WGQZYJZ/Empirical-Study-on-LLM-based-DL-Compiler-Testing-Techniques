
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)

    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + 3 # Addition
        v4  = torch.clamp_min(v2, 0)
        v5  = torch.clamp_max(v4, 6) # Clamp
        v7  = v5 * v2
        v8  = v7 / 6 
        return v8

# Initializing the model
m  = Model()
x1 = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

