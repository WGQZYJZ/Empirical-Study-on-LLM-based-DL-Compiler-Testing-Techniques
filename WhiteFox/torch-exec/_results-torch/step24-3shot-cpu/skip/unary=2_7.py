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
        self.conv_transpose = torch.nn.ConvTranspose2d(1, 7, 2, stride=2, padding=0, bias=True, groups=3, dilation=1)

    def forward(self, x1):
        x1 = self.conv_transpose(x1)
        x1 = torch.flip(x1, [0, 3])
        x2 = x1 * 0.5
        x3 = x1 * x1 * x1
        x4 = x3 * 0.044715
        x5 = x1 + x4
        x6 = x5 * 0.7978845608028654
        x7 = torch.tanh(x6)
        x8 = x7 + 1
        x9 = x2 * x8
        return x9



func = Model().to('cpu')


x1 = torch.randn(2, 1, 7, 13)

test_inputs = [x1]
