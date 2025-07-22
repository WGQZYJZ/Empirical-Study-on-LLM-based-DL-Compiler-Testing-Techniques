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

    def __init__(self, min_val=10, max_val=100):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 1, 1, stride=1, padding=0)
        self.min_val = min_val
        self.max_val = max_val

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, self.min_val - 20)
        v3 = torch.clamp_max(v2 - 255, self.max_val - 20)
        return v3

class Model(torch.nn.Module):

    def __init__(self, min, max):
        raise NotImplementedError('Model must contain one of more layers with the specified pattern.')

    def forward(self, x):
        raise NotImplementedError('Model must pass the specified pattern.')


min = 1
max = 1

func = Model(min, max).to('cpu')


x1 = torch.randn(1, 1, 224, 224)

test_inputs = [x1]
