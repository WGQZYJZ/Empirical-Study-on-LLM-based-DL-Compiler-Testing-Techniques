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

    def forward(x1, x2, x3):
        qk = torch.matmul(x1, x2.transpose(-2, -1)) / math.sqrt(x1.size(-1))
        qk = qk + x3
        attn_weight = torch.softmax(qk, dim=-1)
        output = torch.matmul(x3, x2)
        return output


func = Model().to('cpu')


x1 = torch.randn(3, 4, 5)

x2 = torch.randn(3, 5, 6)

x3 = torch.randn(3, 4, 6)

test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
forward() takes 3 positional arguments but 4 were given

jit:
forward() takes 3 positional arguments but 4 were given
'''