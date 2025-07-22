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
        b = {}
        t1 = torch.full([2048, 1], 1, dtype=b['dtype'], layout=b['layout'], device=b['device'], pin_memory=False)
        t2 = t1.to(device=b['device'])
        return t2



func = Model().to('cpu')


x1 = torch.randn(2048, 1, device='cuda:0')

test_inputs = [x1]

# JIT_FAIL
'''
direct:
'dtype'

jit:
'dtype'
'''