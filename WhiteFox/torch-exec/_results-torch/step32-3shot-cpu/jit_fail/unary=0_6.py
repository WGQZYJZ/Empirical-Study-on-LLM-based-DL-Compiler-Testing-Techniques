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
        self.conv = torch.nn.Conv2d(4, 1, 4, stride=1)
        self.relu = torch.nn.ReLU(inplace=False)

    def forward(self, x1):
        v1 = torch.matmul(x1, x1)
        v2 = v1 * 0.5
        v3 = v1 * v1
        v4 = v3 * v1
        v5 = v4 * 0.044715
        v6 = v1 + v5
        v7 = v6 * 0.7978845608028654
        v8 = v7 * 2.23606797749979
        v9 = torch.tanh(v2)
        v11 = self.conv(x1)
        v12 = v11 * 0.5
        v13 = v11 * v11
        v14 = v13 * v11
        v15 = v14 * 0.044715
        v16 = v11 + v15
        v17 = v16 * 0.7978845608028654
        v18 = v17 * 2.23606797749979
        v19 = v12 * v18
        v20 = v19 + 1
        v21 = torch.flatten(v10, 1)
        v22 = torch.matmul(v10, x1)
        v23 = v22 * 0.5
        v24 = v22 * v22
        v25 = v24 * v22
        v26 = v25 * 0.044715
        v27 = v22 + v26
        v28 = v27 * 0.7978845608028654
        v29 = torch.tanh(v28)
        v30 = v28 + 2.23606797749979
        v31 = v23 * v30
        v32 = torch.squeeze(v31)
        v33 = v32 - 1
        return v33



func = Model().to('cpu')


x1 = torch.randn(128, 256, 512)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [128, 512] but got: [128, 256].

jit:
Failed running call_function <built-in method matmul of type object at 0x7c33acb96ec0>(*(FakeTensor(..., size=(128, 256, 512)), FakeTensor(..., size=(128, 256, 512))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [128, 512] but got: [128, 256].

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''