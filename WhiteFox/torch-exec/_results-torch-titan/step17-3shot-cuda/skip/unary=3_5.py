import os
import torch
import torch.nn.functional as F
import torch.nn as nn
import numpy as np
from torch.autograd import Variable
import math
import torch as th
import torch.linalg as la
from torch.nn import Parameter
import torch.linalg as linalg



class Model(nn.Module):

    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(1, 2, 5, stride=1, padding=2, groups=2)
        self.conv2 = nn.Conv2d(64, 64, 7, stride=1, padding=3, groups=8)
        self.conv3 = nn.Conv2d(8, 8, 1, stride=1, padding=1, groups=1)

    def forward(self, x):
        v1 = self.conv1(x)
        v2 = (v1 * 0.5)
        v3 = (v1 * 0.7071067811865476)
        v4 = torch.erf(v3)
        v5 = (v4 + 1)
        v6 = (v2 * v5)
        v7 = self.conv2(v6)
        v8 = (v7 * 0.5)
        v9 = (v7 * 0.7071067811865476)
        v10 = torch.erf(v9)
        v11 = (v10 + 1)
        v12 = (v8 * v11)
        v13 = self.conv3(v12)
        return v13




func = Model().to('cuda')



x = torch.randn(1, 1, 64, 64, 64)


test_inputs = [x]
