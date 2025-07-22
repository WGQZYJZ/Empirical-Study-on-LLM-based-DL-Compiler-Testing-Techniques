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

    def forward(self, x1, x2):
        return torch.bmm(x1, x2)

    def __call__(self, X, Y):
        return super(Model, self).__call__(X, Y)




func = Model().to('cuda')

x1 = 1
x2 = 1

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
bmm(): argument 'input' (position 1) must be Tensor, not int

jit:
Failed running call_function <built-in method bmm of type object at 0x7d5b0ba699e0>(*(1, 1), **{}):
bmm(): argument 'input' (position 1) must be Tensor, not int

from user code:
   File "<string>", line 24, in __call__
  File "/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/torch/nn/modules/module.py", line 1518, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/torch/nn/modules/module.py", line 1527, in _call_impl
    return forward_call(*args, **kwargs)
  File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''