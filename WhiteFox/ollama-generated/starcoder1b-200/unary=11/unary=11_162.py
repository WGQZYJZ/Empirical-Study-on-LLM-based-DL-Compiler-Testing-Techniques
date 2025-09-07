

# Description of requirements
The model should contain the following pattern:
This pattern characterizes scenarios where the result of a pointwise transposed convolution is added by a constant `5` and then clamped to a minimum of `0`, and a maximum of `8`.


# Model
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1) + 5
        v2 = torch.clamp_min(v1, 0)
        return v2
