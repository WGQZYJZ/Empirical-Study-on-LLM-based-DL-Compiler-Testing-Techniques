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
        self.add = torch.ops.aten.add
        self.expand = torch.ops.aten.expand
        self.linear = torch.nn.Linear(16, 16)
        self.mul = torch.ops.aten.mul
        self.permute = torch.ops.aten.permute
        self.relu6 = torch.ops.aten.relu6
        self.sub = torch.ops.aten.sub

    def forward(self, x1):
        v1 = self.permute(x1, (0, 2, 1))
        v2 = self.linear(self.sub(v1, 0.5), self.linear.weight, self.linear.bias)
        v3 = self.mul(v2, 0.25)
        v4 = self.linear(self.sub(v1, 0.5), self.linear.weight.transpose((- 2), (- 1)), self.linear.bias)
        v3 = self.sub(v3, 0.25)
        v4 = self.relu6(v4)
        v4 = self.sub(v3, v4)
        v5 = self.relu6(self.add(v4, 0.25))
        v6 = self.expand(v5, (v5.shape[0], v5.shape[2]))
        v5 = self.mul(v6, self.linear.weight.transpose((- 2), (- 1)))
        v5 = self.expand(v5, (x1.shape[0], x1.shape[2]))
        v5 = self.relu6(v5)
        v5 = self.add(v5, 0.25)
        v5 = self.mul(v5, v3)
        return v5




func = Model().to('cuda')



x1 = torch.randn(1, 2, 16)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 4 were given

jit:
Failed running call_module L__self___linear(*(FakeTensor(..., device='cuda:0', size=(1, 16, 2)), Parameter(FakeTensor(..., device='cuda:0', size=(16, 16), requires_grad=True)), Parameter(FakeTensor(..., device='cuda:0', size=(16,), requires_grad=True))), **{}):
forward() takes 2 positional arguments but 4 were given

from user code:
   File "<string>", line 29, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''