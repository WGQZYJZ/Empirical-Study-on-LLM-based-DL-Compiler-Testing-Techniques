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

    def __init__(self, min_value=(- 1.75), max_value=1.44):
        super().__init__()
        self.to = torch.nn.ConvTranspose2d(3, 3, 3, 1, 1, 1)
        self.act_1 = torch.nn.ReLU6()
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x3):
        v1 = self.to(x3)
        v2 = torch.clamp_min(v1, self.min_value)
        v3 = torch.clamp_max(v2, self.max_value)
        v4 = self.act_1(v3)
        return v4




func = Model().to('cuda')



x3 = torch.randn(1, 3, 32, 32)


test_inputs = [x3]

# JIT_FAIL
'''
direct:
clamp_min() received an invalid combination of arguments - got (Model, float), but expected one of:
 * (Tensor input, Tensor min, *, Tensor out)
 * (Tensor input, Number min, *, Tensor out)


jit:
clamp_min() received an invalid combination of arguments - got (Model, float), but expected one of:
 * (Tensor input, Tensor min, *, Tensor out)
 * (Tensor input, Number min, *, Tensor out)

'''