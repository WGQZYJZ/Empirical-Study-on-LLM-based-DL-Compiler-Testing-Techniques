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



class Reshape(torch.nn.Module):

    def __init__(self):
        super(Reshape, self).__init__()
        self.fc = torch.nn.Linear(12, 8)

    def forward(self, x1):
        x1 = x1.view((- 1), 2, 3, 2)
        return self.fc(x1)




class Model(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.Reshape = Reshape()

    def forward(self, x1):
        v1 = self.Reshape(x1)
        return (x1 + v1)




func = Model().to('cuda')



x1 = torch.randn(5, 48)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (120x2 and 12x8)

jit:
Failed running call_module L__self___Reshape_fc(*(FakeTensor(..., device='cuda:0', size=(20, 2, 3, 2)),), **{}):
a and b must have same reduction dim, but got [120, 2] X [12, 8].

from user code:
   File "<string>", line 35, in forward
  File "/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/torch/nn/modules/module.py", line 1527, in _call_impl
    return forward_call(*args, **kwargs)
  File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''