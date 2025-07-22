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
        self.conv_t = torch.nn.Conv2d(3, 16, 2, stride=1, groups=2, bias=False)

    def forward(self, x):
        x1 = self.conv_t(x)
        x2 = x1 > 0
        x3 = x1 * 1.34
        x4 = torch.where(x2, x1, x3)
        return x1



func = Model().to('cpu')


x = torch.randn(5, 3, 16, 16)

test_inputs = [x]
