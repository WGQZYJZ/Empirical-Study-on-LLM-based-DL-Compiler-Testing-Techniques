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

    def __init__(self, negative_slope):
        super().__init__()
        self.linear = torch.nn.Linear(2, 3)
        self.negative_slope = negative_slope

    def forward(self, x1):
        v1 = self.linear(x1)
        slope = np.array([self.negative_slope, self.negative_slope])
        v2 = (v1 > 0)
        v3 = (v1 * slope)
        v4 = torch.where(v2, v1, v3)
        return v4



negative_slope = 1
func = Model(0.25).to('cuda')



x1 = torch.randn(1, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
can't convert cuda:0 device type tensor to numpy. Use Tensor.cpu() to copy the tensor to host memory first.

jit:
Failed running call_function <built-in function mul>(*(FakeTensor(..., device='cuda:0', size=(1, 3)), FakeTensor(..., size=(2,), dtype=torch.float64)), **{}):
Attempting to broadcast a dimension of length 2 at -1! Mismatching argument at index 1 had torch.Size([2]); but expected shape should be broadcastable to [1, 3]

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''