# Description of requirements
The model should contain the following pattern:
This pattern characterizes scenarios where a pointwise convolution is applied to an input tensor, and then the ReLU (Rectified Linear Unit) activation function is applied to the output of the convolution. This is a common pattern in convolutional neural networks, where the ReLU function is used to introduce non-linearity after each convolution operation.

# Model
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv(x1)
        return v1 + 0.5
