
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1) + other
        return v1


# Inputs to the model
other = torch.randn(8)  # The size of other tensor should be compatible with output dimensions of "self.conv".
