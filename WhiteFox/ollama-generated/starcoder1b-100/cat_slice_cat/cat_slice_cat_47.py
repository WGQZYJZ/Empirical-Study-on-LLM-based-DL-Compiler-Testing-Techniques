
# Description of requirements
The model should contain the following pattern:
This pattern characterizes scenarios where the output of a pointwise convolution is added together, and then multiplied by another constant `1`, and then multiplied by the original output of the convolution.


# Model
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v0 = self.conv(x1)
        v1 = v0 + 1
        return v1
