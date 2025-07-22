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

    def forward(self, x1, x2):
        v1 = torch.mm(x1, y)
        t1 = torch.cat([v1, v1], 0)
        t2 = torch.cat([t1, t1, t1, t1], 2)
        t3 = torch.cat([t1, t1, t1], 1)
        t4 = torch.cat([t3, t3, t3, t3], 1)
        return torch.cat([t4, t4], 1)




func = Model().to('cuda')



x1 = torch.randn(2, 2)



x2 = torch.randn(3, 2)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu! (when checking argument for argument mat2 in method wrapper_CUDA_mm)

jit:
Failed running call_function <built-in method mm of type object at 0x78286e4699e0>(*(FakeTensor(..., device='cuda:0', size=(2, 2)), FakeTensor(..., size=(2, 2))), **{}):
Unhandled FakeTensor Device Propagation for aten.mm.default, found two different devices cuda:0, cpu

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''