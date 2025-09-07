
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        v1 = self.conv(x1) - x2
        v2 = torch.relu(v1)
        return v2


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
other = torch.rand(8,) * 0.5 # Tensor containing a constant "0.5" in floating-point format
