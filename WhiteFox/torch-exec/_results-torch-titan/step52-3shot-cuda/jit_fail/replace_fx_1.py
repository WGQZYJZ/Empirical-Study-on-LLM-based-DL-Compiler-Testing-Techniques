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
        y1 = torch.rand_like(x1, dtype=torch.float64, layout=torch.strided, device=x1.device, pin_memory=True, requires_grad=False, memory_format=torch.contiguous_format)
        b1 = F.dropout(x1, p=0.8)
        return y1




func = Model().to('cuda')



x1 = torch.randn(1, 2, 3, 4)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Only dense CPU tensors can be pinned

jit:
backend='inductor' raised:
TypeError: rand() received an invalid combination of arguments - got (list, memory_format=torch.memory_format, pin_memory=bool, layout=torch.layout, device=torch.device, dtype=torch.dtype), but expected one of:
 * (tuple of ints size, *, torch.Generator generator, tuple of names names, torch.dtype dtype, torch.layout layout, torch.device device, bool pin_memory, bool requires_grad)
 * (tuple of ints size, *, torch.Generator generator, Tensor out, torch.dtype dtype, torch.layout layout, torch.device device, bool pin_memory, bool requires_grad)
 * (tuple of ints size, *, Tensor out, torch.dtype dtype, torch.layout layout, torch.device device, bool pin_memory, bool requires_grad)
 * (tuple of ints size, *, tuple of names names, torch.dtype dtype, torch.layout layout, torch.device device, bool pin_memory, bool requires_grad)


While executing %rand_like : [num_users=1] = call_function[target=torch.rand_like](args = (%l_x1_,), kwargs = {dtype: torch.float64, layout: torch.strided, device: cuda:0, pin_memory: True, requires_grad: False, memory_format: torch.contiguous_format})
Original traceback:
  File "<string>", line 21, in forward



You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''