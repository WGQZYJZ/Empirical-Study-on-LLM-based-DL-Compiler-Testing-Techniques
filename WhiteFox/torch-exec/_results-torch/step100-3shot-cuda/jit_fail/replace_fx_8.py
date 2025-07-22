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
        x2 = F.dropout(x1, x1, p=0.1)
        x3 = torch.rand_like(x1)
        x4 = x2 + x3
        x5 = torch.rand_like(x1)
        x6 = x2 + x3 + x5
        return (x2, x4, x6)



func = Model().to('cuda')


x1 = torch.randn(1, 16, 16)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
dropout() got multiple values for argument 'p'

jit:
dropout() got multiple values for argument 'p'
'''