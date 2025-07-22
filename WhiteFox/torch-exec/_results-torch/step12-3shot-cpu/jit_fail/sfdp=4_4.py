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
        self.dense_qkv = torch.nn.Linear(64, 512)
        self.scale = math.sqrt(512)

    def forward(x64):
        (q, k, v) = self.dense_qkv(x64).chunk(3, dim=-1)
        q /= self.scale
        k /= self.scale
        out = torch.matmul(q, k.transpose(-2, -1))
        return out


func = Model().to('cpu')


x64 = torch.randn(5, 64)

test_inputs = [x64]

# JIT_FAIL
'''
direct:
forward() takes 1 positional argument but 2 were given

jit:
forward() takes 1 positional argument but 2 were given
'''