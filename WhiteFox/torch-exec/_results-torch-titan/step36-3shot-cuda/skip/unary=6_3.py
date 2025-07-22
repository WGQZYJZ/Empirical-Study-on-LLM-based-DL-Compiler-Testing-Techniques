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



class Model(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 3, 1, stride=1, padding=1, groups=2)
        self.bn = torch.nn.BatchNorm2d(3)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = (3 + v1)
        v3 = torch.clamp_min(v2, 0)
        v4 = torch.clamp_max(v3, 6)
        v5 = (v1 * v4)
        v6 = (v5 / 6)
        v7 = self.bn(v6)
        return v7




func = Model().to('cuda')



x_1 = torch.randn(1, 3, 256, 256)


test_inputs = [x_1]
