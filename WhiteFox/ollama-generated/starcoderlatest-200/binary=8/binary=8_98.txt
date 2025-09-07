
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        if other is not None:
            self.add = torch.nn.ConstantPad2d(((0,0),(1,0),(0,0),(0,0)), other)

    def forward(self, x):
        v1 = self.conv(x) + (self.add if self.add else 0.)
        return v1

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
other_tensor = torch.zeros(1, 8, 64, 64).random_(device=x1.device, dtype=x1.dtype)
m = Model(other_tensor)
