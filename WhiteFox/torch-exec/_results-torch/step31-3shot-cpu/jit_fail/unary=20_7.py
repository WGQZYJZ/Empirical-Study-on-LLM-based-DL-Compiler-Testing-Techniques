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

    def forward(self, x1):
        v1 = torch.nn.functional.conv_transpose2d(x1, None, kernel_size=(9, 9), stride=(2, 2), padding=(1, 1))
        v2 = torch.sigmoid(v1)
        return v2



func = Model().to('cpu')


x1 = torch.randn(1, 16, 14, 14)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
conv_transpose2d(): argument 'weight' (position 2) must be Tensor, not NoneType

jit:
conv_transpose2d(): argument 'weight' (position 2) must be Tensor, not NoneType
'''