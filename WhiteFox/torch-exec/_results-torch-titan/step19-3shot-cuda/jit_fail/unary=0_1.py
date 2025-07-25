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
        self.conv = torch.nn.Conv2d(4, 9, 3, stride=2, padding=3)
        self.bn = torch.nn.BatchNorm2d(9)
        self.softmax = torch.nn.Softmax(0)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.bn(v1)
        v3 = (v2 * 0.5)
        v4 = (v2 * v2)
        v5 = (v4 * v2)
        v6 = (v5 * 0.044715)
        v7 = (v2 + v6)
        v8 = (v7 * 0.7978845608028654)
        v9 = torch.tanh(v8)
        v10 = (v9 + 1)
        v11 = (v3 * v10)
        v12 = self.softmax(v11)
        v13 = torch.transpose(v11, 0, 1)
        v14 = torch.nn.functional.unfold(v13, 3, stride=3)
        v15 = torch.transpose(v14, 1, 2)
        v16 = torch.softmax(v13, 0)
        v17 = torch.transpose(v16, 0, 1)
        v18 = torch.nn.functional.unfold(v17, 3, stride=3)
        v19 = torch.transpose(v18, 1, 2)
        v20 = torch.softmax(v17, 0)
        v21 = torch.add(v1, v15)
        v22 = torch.nn.functional.relu(v21)
        v23 = (v20 + v21)
        v24 = torch.transpose(v11, 0, 1)
        v25 = torch.transpose(v14, 1, 2)
        v26 = torch.softmax(v13, (- 1))
        v27 = torch.transpose(v26, 0, 1)
        v28 = torch.nn.functional.relu(v25)
        v29 = torch.bmm(v24, v27)
        v30 = (v28 + v29)
        v31 = torch.transpose(v13, 0, 1)
        v32 = torch.transpose(v16, 1, 2)
        v33 = torch.pow(v31, (- 0.5))
        v34 = torch.transpose(v32, 0, 1)
        v35 = (v33 * v34)
        v36 = torch.transpose(v35, 1, 2)
        v37 = (v33 + v34)
        v38 = torch.nn.functional.relu(v36)
        v39 = (v37 * v38)
        return v39




func = Model().to('cuda')



x1 = torch.randn(1, 4, 84, 95)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (50) must match the size of tensor b (9) at non-singleton dimension 3

jit:
Failed running call_function <built-in method add of type object at 0x766aaf4699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 9, 44, 50)), FakeTensor(..., device='cuda:0', size=(9, 224, 9))), **{}):
Attempting to broadcast a dimension of length 9 at -1! Mismatching argument at index 1 had torch.Size([9, 224, 9]); but expected shape should be broadcastable to [1, 9, 44, 50]

from user code:
   File "<string>", line 44, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''