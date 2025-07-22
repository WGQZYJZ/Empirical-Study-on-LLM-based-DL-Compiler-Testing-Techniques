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
        v1 = torch.reshape(x1, [(x1.size(0) * x1.size(1)), x1.size(2)])
        v2 = torch.reshape(x2, [(x2.size(0) * x2.size(1)), x2.size(2)])
        v3 = torch.matmul(v1, v2.transpose(0, 1))
        v4 = (v3 / scaling_factor)
        v5 = torch.softmax(v4, dim=(- 1))
        v6 = torch.nn.functional.dropout(v5, p=dropout_probability)
        v7 = torch.matmul(v6, v3)
        return torch.reshape(v7, [(v7.size(0) // x2.size(0)), x1.size(1), x2.size(1)])



func = Model().to('cuda')



x1 = torch.randn(64, 2, 1280)



x2 = torch.randn(256, 2, 1280)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 3 were given

jit:
forward() takes 2 positional arguments but 3 were given
'''