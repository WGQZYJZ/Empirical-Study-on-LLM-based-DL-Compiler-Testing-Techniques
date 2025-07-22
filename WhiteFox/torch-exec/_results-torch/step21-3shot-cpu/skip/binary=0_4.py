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

    def __init__(self, weight1=None):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 2, 3, stride=2, padding=1, _non_persistent_buffers_set=None, weight=weight1, bias=None, dilation=2)

    def forward(self, x):
        v1 = self.conv(x)
        return v1



func = Model().to('cpu')


x = torch.randn(1, 1, 224, 224)

weight = torch.randn(2, 1, 3, 3)

test_inputs = [x, weight]
