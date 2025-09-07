
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, x3):
        v1 = self._conv_t1(x1)
        v2 = _mul(v1, 0.5) # Multiply the output of the convolution by 0.5
        v3 = _mul(v1, 0.7071067811865476)  # Multiply the output of the convolution by 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = _add(_mul(v2, v4), 1)  # Add 1 to the output of the error function
        v6 = _mul(v2, v5)  # Multiply the output of the convolution by the output of the error function
        return v6
 
    def _conv_t1(self, x1):
        conv = torch.nn.Conv2d(3, 8, kernel_size=1, stride=1, padding=0)
        out = conv(x1)
        return out

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 3, 32, 32)
x3 = torch.randn(1, 8, 32, 32)
