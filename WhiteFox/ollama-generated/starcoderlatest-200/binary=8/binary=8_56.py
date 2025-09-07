
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, other=None):
        v1 = self.conv(x1)
        v2 = v1 + (other if other is not None else 0.5) # Note that the default value of other tensor is 0.5
        return v6

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.ones(1, 8, 64, 64)
