import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self, min_value=159620.0, max_value=546218.0):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(22, 16, (12, 15), stride=(5, 5), padding=(6, 6))
        self.min_value = min_value
        self.max_value = max_value
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = torch.clamp_min(v1, self.min_value)
        v3 = torch.clamp_max(v2, self.max_value)
        return v3
m = Model()
# Inputs to the model
x1 = torch.randn(1, 22, 51, 51)
