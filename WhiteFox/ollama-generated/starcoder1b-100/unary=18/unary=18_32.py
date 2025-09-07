
# Description of requirements
The model should contain the following pattern:
This pattern characterizes scenarios where the output of a pointwise convolution is multiplied by another constant `1` and then the Tanh function is applied to the output of the convolution, and then the output of the convolution is added with 1 to it.


# Model
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        return v2 = torch.tanh(v1) + 1


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
