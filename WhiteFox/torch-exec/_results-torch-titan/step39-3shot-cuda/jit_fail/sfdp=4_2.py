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

    def forward(self, d0, d1, mask):
        d = (d0 + d1)
        attn_weight = torch.softmax((((d @ d.transpose((- 2), (- 1))) / math.sqrt(d0.size((- 1)))) + mask), dim=(- 1))
        output = (attn_weight @ d)
        return output




func = Model().to('cuda')



Q = torch.randn(1, 64, 56, 56)



K = torch.randn(1, 64, 56, 56)



V = torch.randn(1, 64, 56, 56)



mask = (torch.rand(1, 56, 56) > 0.7).fill_((- 1000000000.0))


test_inputs = [Q, K, V, mask]

# JIT_FAIL
'''
direct:
forward() takes 4 positional arguments but 5 were given

jit:
forward() takes 4 positional arguments but 5 were given
'''