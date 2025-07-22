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

    def forward(self, x1, x2):
        qk = (x1 @ x2.transpose(1, 2))
        attn_mask = ((torch.triu(x2[:(- 1), :(- 1)]) + torch.tril(x2[:(- 1), :(- 1)])) * (- 10000.0))
        attn_weight = torch.softmax(qk, dim=(- 1))
        output = (attn_weight @ x2)
        return (None, None)



func = Model().to('cuda')



x1 = torch.randn(2, 10, 3)



x2 = torch.randn(2, 10, 4)



x3 = torch.randn(2, 10, 4)



x4 = torch.randn(2, 10, 4)


test_inputs = [x1, x2, x3, x4]

# JIT_FAIL
'''
direct:
forward() takes 3 positional arguments but 5 were given

jit:
forward() takes 3 positional arguments but 5 were given
'''