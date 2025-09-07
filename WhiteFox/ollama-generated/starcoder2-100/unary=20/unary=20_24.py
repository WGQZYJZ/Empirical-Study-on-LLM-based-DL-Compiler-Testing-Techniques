

import torch

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
        self.deconv = torch.nn.ConvTranspose2d(8, 10, 4, stride=2)

    def forward(self, x):
        v1 = self.conv(x)
        v2 = v1 + 1
        v3 = v2 / 0.75

        return v3

m = Model()

