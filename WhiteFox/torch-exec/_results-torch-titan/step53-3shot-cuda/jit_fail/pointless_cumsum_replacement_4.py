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
        b['dtype'] = torch.float16
        b['layout'] = torch.contiguous_format
        b['device'] = torch.device('cuda:0')
        a['dtype'] = torch.int32
        a['layout'] = torch.strided
        a['device'] = torch.device('cuda:0')
        a['dtype_to'] = torch.int64
        a['dtype_from'] = torch.int32
        b['dtype_to'] = torch.int32
        b['dtype_from'] = torch.int64
        t1 = torch.full([2048, 16384], 1, dtype=b['dtype'], layout=b['layout'], device=b['device'], pin_memory=False)
        t2 = t1.to(dtype=a['dtype'])
        t3 = torch.cumsum(t2, 1)
        return t3




func = Model().to('cuda')



x1 = torch.randn(2048, 16384, device='cuda:0')


test_inputs = [x1]

# JIT_FAIL
'''
direct:
full() received an invalid combination of arguments - got (list, int, pin_memory=bool, device=torch.device, layout=torch.memory_format, dtype=torch.dtype), but expected one of:
 * (tuple of ints size, Number fill_value, *, tuple of names names, torch.dtype dtype, torch.layout layout, torch.device device, bool pin_memory, bool requires_grad)
 * (tuple of ints size, Number fill_value, *, Tensor out, torch.dtype dtype, torch.layout layout, torch.device device, bool pin_memory, bool requires_grad)


jit:
Failed running call_function <built-in method full of type object at 0x7c62b4e699e0>(*([2048, 16384], 1), **{'dtype': torch.float16, 'layout': torch.contiguous_format, 'device': device(type='cuda', index=0), 'pin_memory': False}):
full() received an invalid combination of arguments - got (immutable_list, int, pin_memory=bool, device=torch.device, layout=torch.memory_format, dtype=torch.dtype), but expected one of:
 * (tuple of ints size, Number fill_value, *, tuple of names names, torch.dtype dtype, torch.layout layout, torch.device device, bool pin_memory, bool requires_grad)
 * (tuple of ints size, Number fill_value, *, Tensor out, torch.dtype dtype, torch.layout layout, torch.device device, bool pin_memory, bool requires_grad)


from user code:
   File "<string>", line 33, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''