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

    def forward(self, x1):
        v1 = torch.matmul(x1, x2.transpose(-2, -1))
        v2 = v1 / __scale_factor__
        v3 = v2.softmax(dim=-1)
        v4 = torch.nn.functional.dropout(v3, __dropout_p__)
        output = torch.matmul(v4, x3)
        return output


func = Model().to('cuda')


x1 = torch.randn(1, 25, 768)

x2 = torch.randn(1, 25, 768)

x3 = torch.randn(1, 25, 768)

test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 4 were given

jit:
forward() takes 2 positional arguments but 4 were given
'''