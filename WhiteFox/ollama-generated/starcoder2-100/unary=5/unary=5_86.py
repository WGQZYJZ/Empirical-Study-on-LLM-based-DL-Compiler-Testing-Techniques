
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5
        return v6

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

import torch

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(in_channels=3, out_channels=8, kernel_size=1, stride=1)

    def forward(self, x):

        v1  = self.conv_transpose(x)
        v2  = v1 * .5
        v3  = v1 * .7071067811865476
        v4  = torch.erf(v3)
        v5  = v4 + 1
        v6  = v2*v5
        return v6

# Initializing the model with random tensors for the input
x  = .0*torch.randn(size=(8, 3, 28, 28)) # Use a batch size of 1 and shape (3, 28, 28)
m  = Model()
__output__  = m(x)

