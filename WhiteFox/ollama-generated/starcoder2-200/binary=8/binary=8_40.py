
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x):
        v0 = torch.rand_like(x, dtype=torch.float64).detach().requires_grad_(True)
        v1 = self.conv(v0)
        v2 = v1 + v0
        return v2

# Initializing the model
m = Model()

 # Inputs to the model
x  = torch.randn(1, 3, 64, 64)
