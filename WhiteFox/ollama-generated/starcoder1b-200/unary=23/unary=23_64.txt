
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.tanh(v1)
        return v2


# Inputs to the model
__input__  = torch.randn(1, 3, 64, 64)
x1        = __input__.clone()
x2        = Model()(x1)

# Error checking
assert (x1 == x2).all().item()

