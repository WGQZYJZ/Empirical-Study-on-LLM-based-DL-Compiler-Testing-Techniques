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
        self.linear1 = torch.nn.Linear(512, 1024)
        self.linear2 = torch.nn.Linear(1024, 1024)
        self.linear3 = torch.nn.Linear(1024, 1000)

    def forward(self, tensor):
        v1 = self.linear1(tensor)
        v2 = v1 + self.linear2.weight
        v3 = v2 + self.linear2.bias
        v4 = v3 + self.linear3.weight
        v5 = v4 + self.linear3.bias
        return_tensor = []
        idx = 1
        for i in range(64):
            return_tensor.append(v5[idx])
            idx += 64
        return return_tensor


func = Model().to('cpu')


x1 = torch.randn(1024, 512)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (1024) must match the size of tensor b (1000) at non-singleton dimension 0

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(1024, 1024)), Parameter(FakeTensor(..., size=(1000, 1024), requires_grad=True))), **{}):
Attempting to broadcast a dimension of length 1000 at -2! Mismatching argument at index 1 had torch.Size([1000, 1024]); but expected shape should be broadcastable to [1024, 1024]

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''