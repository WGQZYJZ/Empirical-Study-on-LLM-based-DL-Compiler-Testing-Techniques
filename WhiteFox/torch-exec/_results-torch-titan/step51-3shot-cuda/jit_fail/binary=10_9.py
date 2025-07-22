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

    def __init__(self, weight_shape, bias_shape):
        super().__init__()
        self.linear = torch.nn.Linear(*weight_shape)
        self.addition_weight = torch.nn.Parameter(torch.zeros(bias_shape, dtype=torch.float32))

    def forward(self, x1):
        return torch.nn.functional.linear(x1, (self.linear.weight + self.addition_weight))




weight_shape = (3, 4)


bias_shape = (4,)

func = Model(weight_shape, bias_shape).to('cuda')



x1 = torch.randn(2, 3)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (3) must match the size of tensor b (4) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(Parameter(FakeTensor(..., device='cuda:0', size=(4, 3), requires_grad=True)), Parameter(FakeTensor(..., device='cuda:0', size=(4,), requires_grad=True))), **{}):
Attempting to broadcast a dimension of length 4 at -1! Mismatching argument at index 1 had torch.Size([4]); but expected shape should be broadcastable to [4, 3]

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''