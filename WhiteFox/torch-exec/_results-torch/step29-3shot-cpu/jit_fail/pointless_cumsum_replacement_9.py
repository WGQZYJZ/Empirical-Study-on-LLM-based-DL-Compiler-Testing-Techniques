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
        b['dtype'] = torch.cuda.FloatTensor
        b['layout'] = torch.strided
        b['device'] = torch.device('cpu')
        a['dtype'] = torch.cuda.FloatTensor
        a['layout'] = torch.strided
        a['device'] = torch.device('cpu')
        a['dtype_to'] = torch.cuda.FloatTensor
        a['dtype_from'] = torch.cuda.FloatTensor
        b['dtype_to'] = torch.cuda.FloatTensor
        b['dtype_from'] = torch.cuda.FloatTensor
        t1 = torch.full([65632, 3840], 1, dtype=b['dtype'], layout=b['layout'], device=b['device'], pin_memory=False)
        t2 = t1.to(dtype=a['dtype'])
        t3 = torch.cumsum(t2, 1)
        return t3



func = Model().to('cpu')


x1 = torch.randn(65632, 3840, device='cpu')

test_inputs = [x1]

# JIT_FAIL
'''
direct:
full() received an invalid combination of arguments - got (list, int, pin_memory=bool, device=torch.device, layout=torch.layout, dtype=torch.tensortype), but expected one of:
 * (tuple of ints size, Number fill_value, *, tuple of names names, torch.dtype dtype = None, torch.layout layout = None, torch.device device = None, bool pin_memory = False, bool requires_grad = False)
 * (tuple of ints size, Number fill_value, *, Tensor out = None, torch.dtype dtype = None, torch.layout layout = None, torch.device device = None, bool pin_memory = False, bool requires_grad = False)


jit:
NotImplementedError: argument of type: <class 'torch.tensortype'>

from user code:
   File "<string>", line 31, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''