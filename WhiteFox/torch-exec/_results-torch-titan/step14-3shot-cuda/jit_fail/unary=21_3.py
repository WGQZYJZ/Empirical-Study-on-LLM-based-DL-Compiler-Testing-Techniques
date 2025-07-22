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



class ModelTanh(nn.Module):

    def forward(self, x):
        v = nn.Tanh()(x)
        return v[:, :, :, :]




func = ModelTanh().to('cuda')

x = 1

test_inputs = [x]

# JIT_FAIL
'''
direct:
tanh(): argument 'input' (position 1) must be Tensor, not int

jit:
Failed running call_function <built-in method tanh of type object at 0x742ba38699e0>(*(1,), **{}):
tanh(): argument 'input' (position 1) must be Tensor, not int

from user code:
   File "<string>", line 18, in forward
  File "/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/torch/nn/modules/module.py", line 1527, in _call_impl
    return forward_call(*args, **kwargs)
  File "/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/torch/nn/modules/activation.py", line 356, in forward
    return torch.tanh(input)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''