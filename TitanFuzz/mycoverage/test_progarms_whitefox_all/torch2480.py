import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(2, 5, 3, stride=1)
        self.conv2 = torch.nn.Conv2d(5, 9, 4, stride=(2, 3), padding=2)
        self.conv3 = torch.nn.Conv2d(9, 2, 6, stride=1, padding=8)
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = v1 * 0.5
        v3 = v1 * v1 * v1
        v4 = v3 * 0.044715
        v5 = v1 + v4
        v6 = v5 * 0.7978845608028654
        v7 = torch.tanh(v6)
        v8 = v7 + 1
        v9 = v2 * v8
        v10 = self.conv2(v9)
        v11 = v10 * 0.5
        v12 = v10 * v10 * v10
        v13 = v12 * 0.044715
        v14 = v10 + v13
        v15 = v14 * 0.7978845608028654
        v16 = torch.tanh(v15)
        v17 = v16 + 1
        v18 = v11 * v17
        v19 = self.conv3(v18)
        return v19
m = Model()
# Inputs to the model
x1 = torch.randn(7, 2, 10, 4)
