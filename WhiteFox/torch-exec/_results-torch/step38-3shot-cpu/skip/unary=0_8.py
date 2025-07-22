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
        self.batch_norm = torch.nn.BatchNorm2d(33)
        self.conv = torch.nn.Conv2d(33, 9, 7, stride=1, padding=3, groups=9)

    def forward(self, x):
        v1 = self.batch_norm(x)
        v2 = self.conv(v1)
        v3 = v2 * 0.5
        v4 = v2 * v2
        v5 = v4 * v2
        v6 = v5 * 0.044715
        v7 = v2 + v6
        v8 = v7 * 0.7978845608028654
        v9 = torch.relu(v8)
        v10 = v9 + 1
        v11 = v3 * v10
        return v11



func = Model().to('cpu')


x = torch.randn(1, 33, 81, 42)

test_inputs = [x]
