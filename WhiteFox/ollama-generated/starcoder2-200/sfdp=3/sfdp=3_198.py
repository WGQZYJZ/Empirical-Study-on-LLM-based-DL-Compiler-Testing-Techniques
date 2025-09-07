

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v1  = self.conv(x1) # Apply pointwise convolution with kernel size 1 to the input tensor

        v2 = v1 * 0.5 # Multiply the output of the convolution by 0.5
        v3 = v1 + 0.7071067811865476 # Add 0.7071067811865476 to the output of the convolution

        v4 = torch.erf(v3)
        v5 = v4 + 2 * self.conv(x1) # Add twice (pointwise convolution with kernel size 1 to the input tensor) to the error function and apply it on the output of the convolution

        v6 = v2 * v5
        return v6

m = Model()

 x1 = torch.randn(4,3,8,9)

__output__  = m(x1)

