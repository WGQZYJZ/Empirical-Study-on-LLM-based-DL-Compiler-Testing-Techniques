

# Model
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1, x2):
        v1 = self.conv(x1) > 0
        v2 = self.conv(x2) * -self.negative_slope
        v3 = torch.where(v1, x1, x2)
        return v3


# Test the models and generate the corresponding input tensors
# Inputs to the model
x1 = torch.randn(2, 3, 64, 64)
y1 = torch.randn(2, 8)
__output1__ = m(x1, y1)


# Inputs to the model
x2 = torch.randn(1, 3, 64, 64)
__output2__ = m(x2)


