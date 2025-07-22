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
        self.conv = torch.nn.Conv2d(32, 64, kernel_size=(1, 1), stride=(1, 1), padding=(0, 0), dilation=(1, 1), groups=1, bias=True)
        nn.init.constant_(self.conv.weight.data, 0.11390784328985329)
        nn.init.constant_(self.conv.bias.data, 0.2092717409601135)

    def forward(self, x1):
        y = F.conv_transpose2d(x1, self.conv.weight, self.conv.bias, stride=None, padding=None, output_padding=1, groups=1, dilation=1, padding_mode='zeros', benchmark=True, deterministic=False)
        return y



func = Model().to('cpu')

x1 = 1

test_inputs = [x1]

# JIT_FAIL
'''
direct:
conv_transpose2d(): argument 'input' (position 1) must be Tensor, not int

jit:
conv_transpose2d(): argument 'input' (position 1) must be Tensor, not int
'''