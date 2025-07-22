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
        self.conv_transpose1 = torch.nn.ConvTranspose2d(2, 9, 3, stride=1, padding=2)
        self.conv_transpose2 = torch.nn.ConvTranspose1d(9, 6, 4, stride=2, padding=1)
        self.conv_transpose3 = torch.nn.ConvTranspose1d(6, 2, 2, stride=1, padding=0)

    def forward(self, x1):
        t1 = self.conv_transpose1(x1)
        t2 = t1 * 0.5
        t3 = t1 * 0.7071067811865476
        t4 = torch.erf(t3)
        t5 = t4 + 1
        t6 = t2 * t5
        t7 = self.conv_transpose2(t6)
        t8 = t7 * 0.5
        t9 = t7 * 0.7071067811865476
        t10 = torch.erf(t9)
        t11 = t10 + 1
        t12 = t8 * t11
        t13 = self.conv_transpose3(t12)
        t14 = t13 * 0.5
        t15 = t13 * 0.7071067811865476
        t16 = torch.erf(t15)
        t17 = t16 + 1
        x2 = t14 * t17
        return x2



func = Model().to('cpu')


x1 = torch.randn(1, 2, 16, 16)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected 2D (unbatched) or 3D (batched) input to conv_transpose1d, but got input of size: [1, 9, 14, 14]

jit:
Failed running call_function <built-in method conv_transpose1d of type object at 0x7ef2df196ec0>(*(FakeTensor(..., size=(1, 9, 14, 14)), Parameter(FakeTensor(..., size=(9, 6, 4), requires_grad=True)), Parameter(FakeTensor(..., size=(6,), requires_grad=True)), (2,), (1,), (0,), 1, (1,)), **{}):
Expected 2D (unbatched) or 3D (batched) input to conv_transpose1d, but got input of size: [1, 9, 14, 14]

from user code:
   File "<string>", line 28, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 974, in forward
    return F.conv_transpose1d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''