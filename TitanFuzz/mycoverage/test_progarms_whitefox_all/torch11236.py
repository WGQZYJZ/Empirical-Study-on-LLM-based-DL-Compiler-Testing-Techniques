import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(6, 6, (3,9,9,1,2,2), stride=(1,1,10,1,1,1), padding=(1,2,2,0,1,0))
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5
        return v6
m = Model()
# Inputs to the model
x1 = torch.randn(1, 6, 3, 9, 9, 1, 2, 2)
