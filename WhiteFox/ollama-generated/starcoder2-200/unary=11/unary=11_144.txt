
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + 3 
        v3  = torch.clamp_min(v2, 0)
        v4  = torch.clamp_max(v3, 6)
        return v4 / 6


# Initializing the model
m  = Model()

# Input to the model (same as the previous model): 
x1  = torch.randn(2, 3, 80, 70)

__output__  = m(x1)
