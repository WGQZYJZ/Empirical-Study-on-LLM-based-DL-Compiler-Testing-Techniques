
class Model(torch.nn.Module):
    def __init__(self, other_tensor: torch.Tensor=None):
        super().__init__()
        if other_tensor == None:
            self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
            self.other = torch.randn(1, 3, 64, 64)
        else:
            self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv(x1)
        if self.other is not None:
            v2 = v1 + other_tensor
        else:
            v2 = v1
        return v6


# Inputs to the model
m = Model() # m.other == torch.randn(1, 3, 64, 64) (default value)
x1 = torch.randn(1, 3, 64, 64)
