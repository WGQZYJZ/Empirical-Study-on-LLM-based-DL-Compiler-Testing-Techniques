
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5
        return v6


# Generating the input tensor for the model above
import numpy as np
np.random.seed(0)
x = torch.randn(1, 3, 64, 64).numpy() # shape: (1, 3, 64, 64), dtype: float64
x_input = np.copy(x[0])
print('shape:', x_input.shape)
print('dtype:', x_input.dtype)


# User-generated code ends here. Do not delete the line below.
