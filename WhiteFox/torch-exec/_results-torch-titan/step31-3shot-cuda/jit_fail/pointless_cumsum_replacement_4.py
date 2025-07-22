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
        b['device'] = torch.device('cuda:0')
        a['dtype'] = torch.float32
        a['layout'] = torch.strided
        a['device'] = torch.device('cuda:0')
        a['dtype_to'] = torch.float32
        a['dtype_from'] = torch.float32
        b['dtype_to'] = torch.float32
        b['dtype_from'] = torch.float32
        t1 = torch.full([1, 1024], 1.13797082e-10, dtype=b['dtype'], layout=b['layout'], device=b['device'], pin_memory=True)
        t2 = t1.to(dtype=a['dtype'])
        t3 = torch.cumsum(t2, 1)
        return t3




func = Model().to('cuda')



x1 = torch.randn(1, 1024, device='cuda:0')


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Only dense CPU tensors can be pinned

jit:
backend='inductor' raised:
RuntimeError: Only dense CPU tensors can be pinned

While executing %full : [num_users=1] = call_function[target=torch.ops.aten.full.default](args = ([1, 1024], 1.13797082e-10), kwargs = {dtype: torch.float32, layout: torch.strided, device: cuda:0, pin_memory: True})
Original traceback:
  File "<string>", line 33, in forward



You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''