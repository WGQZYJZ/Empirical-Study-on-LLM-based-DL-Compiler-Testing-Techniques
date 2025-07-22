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

    def __init__(self, m):
        super().__init__()
        self.m = m

    def forward(self, x1):
        x2 = self.m(x1)
        x3 = torch.rand(size=(1,))
        x4 = torch.rand(size=(1,))
        x5 = (x3 + x4)
        return torch.rand_like(x5)




class m(torch.nn.Module):

    def __init__(self, a):
        super().__init__()
        self.a = a

    def forward(self, x1):
        x2 = self.a(x1)
        x3 = torch.rand(size=(1,))
        x4 = torch.rand(size=(1,))
        x5 = (x3 + x4)
        return torch.rand_like(x5)




class a(torch.nn.Module):

    def __init__(self):
        super().__init__()

    def forward(self, x1):
        x2 = torch.randint((1,), 0, 2, dtype=torch.int32)
        return torch.nn.functional.relu(x2)




func = a().to('cuda')



x1 = torch.randn(1, 1, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
randint() received an invalid combination of arguments - got (tuple, int, int, dtype=torch.dtype), but expected one of:
 * (int high, tuple of ints size, *, torch.Generator generator, Tensor out, torch.dtype dtype, torch.layout layout, torch.device device, bool pin_memory, bool requires_grad)
 * (int high, tuple of ints size, *, Tensor out, torch.dtype dtype, torch.layout layout, torch.device device, bool pin_memory, bool requires_grad)
 * (int low, int high, tuple of ints size, *, torch.Generator generator, Tensor out, torch.dtype dtype, torch.layout layout, torch.device device, bool pin_memory, bool requires_grad)
 * (int low, int high, tuple of ints size, *, Tensor out, torch.dtype dtype, torch.layout layout, torch.device device, bool pin_memory, bool requires_grad)


jit:
Failed running call_function <built-in method randint of type object at 0x7f8d7ac699e0>(*((1,), 0, 2), **{'dtype': torch.int32}):
randint() received an invalid combination of arguments - got (tuple, int, int, dtype=torch.dtype), but expected one of:
 * (int high, tuple of ints size, *, torch.Generator generator, Tensor out, torch.dtype dtype, torch.layout layout, torch.device device, bool pin_memory, bool requires_grad)
 * (int high, tuple of ints size, *, Tensor out, torch.dtype dtype, torch.layout layout, torch.device device, bool pin_memory, bool requires_grad)
 * (int low, int high, tuple of ints size, *, torch.Generator generator, Tensor out, torch.dtype dtype, torch.layout layout, torch.device device, bool pin_memory, bool requires_grad)
 * (int low, int high, tuple of ints size, *, Tensor out, torch.dtype dtype, torch.layout layout, torch.device device, bool pin_memory, bool requires_grad)


from user code:
   File "<string>", line 53, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''