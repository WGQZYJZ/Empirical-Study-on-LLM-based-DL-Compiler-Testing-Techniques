
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        if isinstance(other, int):
            self.other = torch.ones(1, 8).to(other).type(torch.Tensor)
        else:
            self.other = other
 
    def forward(self, x1, other):
        v1 = self.conv(x1) + self.other
        return v1


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
