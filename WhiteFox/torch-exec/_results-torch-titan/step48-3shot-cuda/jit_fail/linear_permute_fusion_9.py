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
        self.linear = torch.nn.Linear(8, 4)

    def forward(self, x2):
        v0 = x2
        v1 = v0.flatten(1, 2)
        if torch.allclose(v1[:, :, 0], v1[:, :, (- 1)]):
            v1 = (v1 + torch.randn(1, 2, 2))
        v2 = v1.reshape((- 1), 1, 4, 2)
        v3 = (v2 + torch.randn(1, 1, 4, 2))
        v4 = v3.reshape((- 1), 2, 2, 2)
        v5 = v4.permute(0, 2, 3, 1)
        v6 = v5.flatten(1, 2)
        v7 = torch.cat((v6[:, :, 0::2], v6[:, :, 1::2]), 2)
        return v7




func = Model().to('cuda')



x2 = torch.randn(1, 1, 2, 8)


test_inputs = [x2]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu!

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(2, 1, 4, 2)), FakeTensor(..., size=(1, 1, 4, 2))), **{}):
Unhandled FakeTensor Device Propagation for aten.add.Tensor, found two different devices cuda:0, cpu

from user code:
   File "<string>", line 27, in <resume in forward>


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''