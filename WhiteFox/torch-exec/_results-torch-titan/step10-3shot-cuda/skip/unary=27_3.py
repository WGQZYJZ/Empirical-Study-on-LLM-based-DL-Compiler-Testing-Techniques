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

    def __init__(self, min, max):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 4, stride=2, padding=1)
        self.max = torch.nn.Parameter(torch.tensor(0.5, requires_grad=True))
        self.min = min
        self.max = max

    def forward(self, x1):
        v1 = self.conv(x1)
        v1 += self.max
        v2 = torch.clamp_min(v1, self.min)
        v2 += self.max
        v3 = torch.clamp_max(v2, self.max)
        v3 += self.max
        return v3




min = 0.1


max = 0.33


func = Model(min, max).to('cuda')



x1 = torch.randn(1, 3, 32, 32)


test_inputs = [x1]
