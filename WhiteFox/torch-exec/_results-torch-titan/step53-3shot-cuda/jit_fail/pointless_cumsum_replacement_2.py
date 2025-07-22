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

    def forward(self, x2, x3):
        b = {}
        a = {}
        b['dtype'] = torch.double
        b['layout'] = torch.strided
        b['device'] = torch.device('cuda')
        a['dtype'] = torch.float32
        a['layout'] = torch.strided
        a['device'] = torch.device('cuda')
        a['dtype_to'] = torch.float32
        a['dtype_from'] = torch.float64
        b['dtype_to'] = torch.float32
        b['dtype_from'] = torch.float64
        t1 = torch.full([10, 1000, 16000, 1], 1, dtype=b['dtype'], layout=b['layout'], device=b['device'], pin_memory=False)
        t2 = t1.to(dtype=a['dtype'])
        t3 = torch.bmm(t2, x3)
        t4 = torch.randn(1, 1, 1000, 16000, dtype=a['dtype'], layout=a['layout'], device=a['device'], pin_memory=False)
        t5 = t3.mul(t4)
        y1 = torch.ones(t3.size(), dtype=a['dtype'], layout=a['layout'], device=a['device'], pin_memory=False)
        t7 = y1.add(t5)
        t6 = y1.sub(t5)
        y2 = torch.full([16000, 1, 1, 1000], 2, dtype=a['dtype'], layout=a['layout'], device=a['device'], pin_memory=False)
        t8 = torch.mul(t2, y2)
        t9 = torch.add(t7, t8)
        y3 = torch.full([1, 1000, 1024, 256], 3, dtype=a['dtype'], layout=a['layout'], device=a['device'], pin_memory=False)
        t10 = torch.mul(t2, y3)
        t11 = torch.sub(t10, t9)
        y4 = torch.ones(t11.size(), dtype=a['dtype'], layout=a['layout'], device=a['device'], pin_memory=False)
        t13 = y4.add(t11)
        t12 = y4.sub(t11)
        return (t13, t12)




func = Model().to('cuda')



x2 = torch.randn(1000, 16000, device='cuda')



x3 = torch.randn(1024, 256, device='cuda')


test_inputs = [x2, x3]

# JIT_FAIL
'''
direct:
batch1 must be a 3D tensor

jit:
Failed running call_function <built-in method bmm of type object at 0x7c62b4e699e0>(*(FakeTensor(..., device='cuda:0', size=(10, 1000, 16000, 1)), FakeTensor(..., device='cuda:0', size=(1024, 256))), **{}):
batch1 must be a 3D tensor

from user code:
   File "<string>", line 35, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''