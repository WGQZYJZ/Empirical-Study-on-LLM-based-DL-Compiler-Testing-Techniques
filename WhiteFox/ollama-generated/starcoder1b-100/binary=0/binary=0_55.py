
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, other):
        v1 = self.conv(x1) + other  # Pass "other" as a keyword argument to the addition operation
        return v1


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
