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
        self.conv2d_1 = torch.nn.Conv2d(32, 3, 7, stride=1, padding=0)
        self.conv2d = torch.nn.Conv2d(6, 10, 3, stride=1, padding=1)
        self.conv2d_dim1 = torch.nn.Conv2d(3, 4, 3, stride=2, padding=1)
        self.conv2d_dim2 = torch.nn.Conv2d(20, 32, 11, stride=1, padding=5)

    def forward(self, x3, x1, x2):
        v1 = self.conv2d_1(x3)
        v2 = v1 * 0.5
        v3 = v1 * v1
        v4 = v3 * v1
        v5 = v4 * 0.044715
        v6 = v1 + v5
        v7 = v6 * 0.7978845608028654
        v8 = torch.tanh(v7)
        v9 = v8 + 1
        v10 = v2 * v9
        v11 = self.conv2d(x1)
        v12 = v11 * 0.5
        v13 = v11 * v11
        v14 = v13 * v11
        v15 = v14 * 0.044715
        v16 = v11 + v15
        v17 = v16 * 0.7978845608028654
        v18 = torch.tanh(v17)
        v19 = v18 + 1
        v20 = v12 * v19
        v21 = self.conv2d_dim1(x2)
        v22 = v21 * 0.5
        v23 = v21 * v21
        v24 = v23 * v21
        v25 = v24 * 0.044715
        v26 = v21 + v25
        v27 = v26 * 0.7978845608028654
        v28 = torch.tanh(v27)
        v29 = v28 + 1
        v30 = v22 * v29
        v31 = self.conv2d_dim2(x1)
        v32 = v31 * 0.5
        v33 = v31 * v31
        v34 = v33 * v31
        v35 = v34 * 0.044715
        v36 = v31 + v35
        v37 = v36 * 0.7978845608028654
        v38 = torch.tanh(v37)
        v39 = v38 + 1
        v40 = v32 * v39
        v41 = v40 * v30
        v42 = v10 + v41
        return v42



func = Model().to('cpu')


x3 = torch.randn(1, 32, 128, 32)

x1 = torch.randn(1, 6, 32, 32)

x2 = torch.randn(1, 3, 128, 128)

test_inputs = [x3, x1, x2]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [32, 20, 11, 11], expected input[1, 6, 32, 32] to have 20 channels, but got 6 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x72fe7d196ec0>(*(FakeTensor(..., size=(1, 6, 32, 32)), Parameter(FakeTensor(..., size=(32, 20, 11, 11), requires_grad=True)), Parameter(FakeTensor(..., size=(32,), requires_grad=True)), (1, 1), (5, 5), (1, 1), 1), **{}):
Given groups=1, weight of size [32, 20, 11, 11], expected input[1, 6, 32, 32] to have 20 channels, but got 6 channels instead

from user code:
   File "<string>", line 53, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''