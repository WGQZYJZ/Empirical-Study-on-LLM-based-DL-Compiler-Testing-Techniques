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



class m2(torch.nn.Module):

    def forward(self, x):
        tmp1 = x
        m1 = torch.nn.BatchNorm2d(4, affine=False)
        tmp2 = m1(tmp1)
        return tmp2




class Model(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.m2 = m2()

    def forward(self, x):
        tmp1 = x
        m1 = torch.nn.BatchNorm2d(4, affine=False)
        tmp2 = m1(tmp1)
        tmp3 = self.m2(tmp2)
        return tmp3




func = Model().to('cuda')



x1 = torch.randn((2, 2, 2, 2))


test_inputs = [x1]

# JIT_FAIL
'''
direct:
running_mean should contain 2 elements not 4

jit:
Failed running call_function <function batch_norm at 0x757047de4b80>(*(FakeTensor(..., device='cuda:0', size=(2, 2, 2, 2)), FakeTensor(..., size=(4,)), FakeTensor(..., size=(4,)), None, None, True, 0.1, 1e-05), **{}):
running_mean should contain 2 elements not 4

from user code:
   File "<string>", line 35, in <resume in forward>
  File "/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/torch/nn/modules/module.py", line 1527, in _call_impl
    return forward_call(*args, **kwargs)
  File "/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/torch/nn/modules/batchnorm.py", line 171, in forward
    return F.batch_norm(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''