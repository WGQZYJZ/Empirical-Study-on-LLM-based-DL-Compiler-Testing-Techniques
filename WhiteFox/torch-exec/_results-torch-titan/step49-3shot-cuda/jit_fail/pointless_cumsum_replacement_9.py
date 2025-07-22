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
        b['dtype'] = torch.uint8
        b['layout'] = torch.strided
        b['device'] = torch.device('cuda:0')
        a['dtype'] = torch.float64
        a['layout'] = torch.strided
        a['device'] = torch.device('cuda:0')
        a['dtype_to'] = torch.complex128
        a['dtype_from'] = torch.float16
        b['dtype_to'] = torch.float64
        b['dtype_from'] = torch.complex128
        t1 = torch.full([1024, 128], 1, dtype=b['dtype'], layout=b['layout'], device=b['device'], pin_memory=False)
        t11 = t1.to(device='cuda:1')
        t2 = None
        t3 = None
        t33 = torch.bmm(t1, t2.t())
        t4 = t33.to(dtype=a['dtype'])
        t5 = torch.cumsum(t4, 1)
        return t5




func = Model().to('cuda')



x1 = torch.randn(1024, 128, device='cuda:0')


test_inputs = [x1]

# JIT_FAIL
'''
direct:
'NoneType' object has no attribute 't'

jit:
'NoneType' object has no attribute 't'

from user code:
   File "<string>", line 37, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''