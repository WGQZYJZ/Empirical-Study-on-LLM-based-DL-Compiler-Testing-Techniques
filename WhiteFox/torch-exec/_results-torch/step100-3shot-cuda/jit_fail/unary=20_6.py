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
        self.conv_t = torch.nn.ConvTranspose2d(1, 1, kernel_size=(1, 1), stride=(1, 1), padding=(10000, 10000))

    def forward(self, x1):
        v1 = self.conv_t(x1)
        v2 = torch.sigmoid(v1)
        return v2



func = Model().to('cuda')


x1 = torch.randn(1, 1, 6, 6)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Trying to create tensor with negative dimension -19994: [1, 1, -19994, -19994]

jit:
Failed running call_function <built-in method conv_transpose2d of type object at 0x7baf3f996ec0>(*(FakeTensor(..., device='cuda:0', size=(1, 1, s0, s1)), Parameter(FakeTensor(..., device='cuda:0', size=(1, 1, 1, 1), requires_grad=True)), Parameter(FakeTensor(..., device='cuda:0', size=(1,), requires_grad=True)), (1, 1), (10000, 10000), (0, 0), 1, (1, 1)), **{}):
Trying to create tensor with negative dimension s0 - 20000: [1, 1, s0 - 20000, s1 - 20000]

from user code:
   File "<string>", line 20, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 1162, in forward
    return F.conv_transpose2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''