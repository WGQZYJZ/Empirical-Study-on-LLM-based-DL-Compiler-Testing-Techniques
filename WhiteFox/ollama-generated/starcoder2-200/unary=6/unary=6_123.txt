

import torch 

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x):
        v1 = self.conv(x)
        v2 = v1 + 3 
        v3 = torch.clamp_min(v2, 0)
        v4 = torch.clamp_max(v3, 6) 
        v5 = v1 * v4 
        v6 = v5 / 6.0
        return v6


m = Model()

x = torch.randn(1, 3, 64, 64) 

