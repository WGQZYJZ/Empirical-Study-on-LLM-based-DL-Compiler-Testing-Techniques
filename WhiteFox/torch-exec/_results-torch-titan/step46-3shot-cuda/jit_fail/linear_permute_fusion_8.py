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
        self.linear = torch.nn.Linear(2, 5)

    def forward(self, x1):
        v1 = torch.randn(1, 3)
        v2 = torch.randn(2, 2, 2)
        v3 = torch.randn(2, 2, 1)
        v4 = v1.to(v2.dtype)
        v2 = (v2 + v4)
        v4 = v1.to(v2.dtype)
        v2 = (v2 + v4)
        v4 = v1.to(v3.dtype)
        v3 = (v3 + v4)
        v4 = v1.to(v3.dtype)
        v3 = (v3 + v4)
        v15 = v3.reshape([(- 1), ((v1.shape[1] * v2.shape[1]) * v3.shape[2])])
        v14 = v2.reshape([(- 1), (v1.shape[1] * v2.shape[1]), v2.shape[2]])
        v13 = v3.reshape([(- 1), v1.shape[1], (v3.shape[1] * v3.shape[2])])
        v12 = v2.reshape([(- 1), v1.shape[1], (v2.shape[1] * v2.shape[2])])
        v11 = v3.reshape([(- 1), v1.shape[1], (v3.shape[1] * v3.shape[2])])
        v10 = v2.reshape([(- 1), v1.shape[1], (v2.shape[1] * v2.shape[2])])
        v6 = torch.mm(v10, (self.linear.weight.permute(1, 0) * v13))
        v7 = torch.mm(v11, (self.linear.weight.permute(1, 0) * v14))
        v8 = torch.mm(v12, (self.linear.weight.permute(1, 0) * v15))
        v9 = ((v6 + v7) + v8)
        return v9.permute(1, 2, 0)




func = Model().to('cuda')



x1 = torch.randn(1, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (2) must match the size of tensor b (3) at non-singleton dimension 2

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(2, 2, 2)), FakeTensor(..., size=(1, 3))), **{}):
Attempting to broadcast a dimension of length 3 at -1! Mismatching argument at index 1 had torch.Size([1, 3]); but expected shape should be broadcastable to [2, 2, 2]

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''