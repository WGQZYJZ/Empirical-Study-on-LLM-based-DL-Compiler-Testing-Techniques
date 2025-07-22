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
        b['dtype'] = torch.int8
        b['layout'] = torch.strided
        b['device'] = torch.device('cuda:0')
        a['dtype'] = torch.uint8
        a['layout'] = torch.strided
        a['device'] = torch.device('cuda:0')
        a['dtype_to'] = torch.uint8
        a['dtype_from'] = torch.int8
        t1 = torch.full([256, 512], 1, dtype=b['dtype'], layout=b['layout'], device=b['device'], pin_memory=False)
        t2 = torch.quantize_per_tensor(t1, 0.0, 255, torch.quint8)
        t3 = t2.dequantize()
        t4 = t3.to(dtype=a['dtype'])
        return t4



func = Model().to('cpu')


x1 = torch.randn(256, 512, device='cuda:0')

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Quantize only works on Float Tensor, got Char

jit:
Failed running call_function <built-in method quantize_per_tensor of type object at 0x779999596ec0>(*(FakeTensor(..., device='cuda:0', size=(256, 512), dtype=torch.int8), 0.0, 255, torch.quint8), **{}):
Quantize only works on Float Tensor, got Char

from user code:
   File "<string>", line 30, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''