
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1) + other
        return v6


# Inputs to the model
other_tensor = torch.randn(1, 3, 2, 4) # This tensor should not be multiplied by anything in the model above
x1 = torch.randn(1, 3, 64, 64)
