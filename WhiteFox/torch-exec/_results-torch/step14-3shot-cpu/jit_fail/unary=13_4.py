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
        v1 = x1.view(-1)
        v2 = v1.size(0)
        v3 = torch.zeros(v2, dtype=torch.float32, device=torch.device('cuda:0'))
        v4 = torch.sigmoid(v3)
        v5 = v1 * v4
        x2 = v5.view(1, -1)
        return x2


func = Model().to('cpu')



x1 = torch.rand(1, 200, dtype=torch.float32).cuda()

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu!

jit:
Failed running call_function <built-in function mul>(*(FakeTensor(..., size=(200,)), FakeTensor(..., device='cuda:0', size=(200,))), **{}):
Unhandled FakeTensor Device Propagation for aten.mul.Tensor, found two different devices cpu, cuda:0

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''