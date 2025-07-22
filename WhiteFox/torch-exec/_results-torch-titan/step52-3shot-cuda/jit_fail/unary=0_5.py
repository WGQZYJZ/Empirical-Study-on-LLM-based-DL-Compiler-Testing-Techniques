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
        self.conv1d = torch.nn.Conv1d(5, 64, 3, stride=1, padding=1)
        self.conv2d = torch.nn.Conv2d(3, 5, 3, stride=5, padding=0)
        self.conv3d = torch.nn.Conv3d(4, 8, 1, stride=1, padding=1)

    def forward(self, x1, x2, x3):
        v1 = self.conv1d(x1)
        v2 = (v1 * 0.5)
        v3 = (v1 * v1)
        v4 = (v3 * v1)
        v5 = (v4 * 0.044715)
        v6 = (v1 + v5)
        v7 = (v6 * 0.7978845608028654)
        v8 = torch.tanh(v7)
        v9 = (v8 + 1)
        v10 = (v2 * v9)
        v11 = self.conv2d(x2)
        v12 = (v11 * 0.5)
        v13 = (v11 * v11)
        v14 = (v13 * v11)
        v15 = (v14 * 0.044715)
        v16 = (v11 + v15)
        v17 = (v16 * 0.7978845608028654)
        v18 = torch.tanh(v17)
        v19 = (v18 + 1)
        v20 = (v12 * v19)
        v21 = self.conv3d(x3)
        v22 = (v21 * 0.5)
        v23 = (v21 * v21)
        v24 = (v23 * v21)
        v25 = (v24 * 0.044715)
        v26 = (v21 + v25)
        v27 = (v26 * 0.7978845608028654)
        v28 = torch.tanh(v27)
        v29 = (v28 + 1)
        v30 = (v22 * v29)
        v31 = (v10 + v30)
        return v31




func = Model().to('cuda')



x1 = torch.randn(1, 5, 10)



x2 = torch.randn(1, 3, 13, 11)



x3 = torch.randn(1, 4, 5, 5, 5)


test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
The size of tensor a (10) must match the size of tensor b (7) at non-singleton dimension 4

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 64, 10)), FakeTensor(..., device='cuda:0', size=(1, 8, 7, 7, 7))), **{}):
Attempting to broadcast a dimension of length 7 at -1! Mismatching argument at index 1 had torch.Size([1, 8, 7, 7, 7]); but expected shape should be broadcastable to [1, 1, 1, 64, 10]

from user code:
   File "<string>", line 54, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''