
The model should have the following pattern:
This pattern characterizes scenarios where the output of a pointwise convolution is multiplied by another tensor or scalar.

# Model
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, other):
        v1 = self.conv(x1)
        return -v1 * other
