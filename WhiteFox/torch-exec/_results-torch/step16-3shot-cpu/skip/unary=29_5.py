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

    def __init__(self, min_value=-16.5, max_value=4.1):
        super().__init__()
        self.conv2d = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.softmax = torch.nn.Softmax(dim=-1, dtype=torch.float32)
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x1):
        v1 = self.conv2d(x1)
        v2 = torch.clamp_min(v1, self.min_value)
        v3 = torch.clamp_max(v2, self.max_value)
        v4 = self.softmax(v3)
        return v4



func = Model().to('cpu')


x1 = torch.randint(256, (1, 3, 64, 64))

test_inputs = [x1]
