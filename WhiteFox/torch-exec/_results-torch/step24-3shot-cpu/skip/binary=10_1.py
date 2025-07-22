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

    def __init__(self, output_channel, kernel_size, padding=0, bias=False, other=None):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, output_channel, kernel_size, padding=padding, bias=bias)
        self.linear = torch.nn.Linear(output_channel, 8)
        if other is None:
            self.other = self.linear.bias.detach().clone().detach()
        else:
            self.other = other

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + self.other
        v3 = self.linear(v2)
        return v3


output_channel = 1
kernel_size = 1
func = Model(3, 1, other=other).to('cpu')


other = torch.randn(1, 8)

x1 = torch.randn(1, 3, 64, 64)

test_inputs = [other, x1]
