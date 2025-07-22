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
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = (x1 + v1)
        x2 = torch.nn.functional.relu(v2)
        v3 = x2.permute(1, 0, 2)
        v4 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        v5 = (v3.unsqueeze(dim=0) * v2.unsqueeze(dim=0))
        v5 = v5
        v5 = (v5 + torch.eye(v5.shape[(- 1)])[(None, ...)])
        v5 = (v5 + 2)
        v5 = torch.tanh(v5)
        v5 = v5.permute(1, 0, 2)
        v5 = v5.squeeze(dim=(- 1))
        v5 = (v4 / v1)
        return x2




func = Model().to('cuda')



x1 = torch.randn(1, 2, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu!

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 2, 2, 2)), FakeTensor(..., size=(1, 2, 2))), **{}):
Unhandled FakeTensor Device Propagation for aten.add.Tensor, found two different devices cuda:0, cpu

from user code:
   File "<string>", line 29, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''