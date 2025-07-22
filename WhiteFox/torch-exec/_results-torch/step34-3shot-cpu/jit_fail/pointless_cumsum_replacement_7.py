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
        a = {}
        b['dtype'] = torch.float32
        b['layout'] = torch.strided
        b['device'] = torch.device('cuda:1')
        a['dtype'] = torch.half
        a['layout'] = torch.strided
        a['device'] = torch.device('cuda:0')
        a['dtype_to'] = torch.half
        a['dtype_from'] = torch.half
        b['dtype_to'] = torch.full_like(x1, torch.half)
        b['dtype_from'] = torch.half
        t1 = torch.full([256, 1024], 1, dtype=b['dtype'], layout=b['layout'], device=b['device'], pin_memory=False)
        t2 = t1.to(dtype=a['dtype'])
        t3 = torch.cumsum(t2, 1)
        return t3



func = Model().to('cpu')


x1 = torch.randn(256, 1024, device='cuda:1')

test_inputs = [x1]

# JIT_FAIL
'''
direct:
full_like(): argument 'fill_value' (position 2) must be Number, not torch.dtype

jit:
full_like(): argument 'fill_value' (position 2) must be Number, not torch.dtype
'''