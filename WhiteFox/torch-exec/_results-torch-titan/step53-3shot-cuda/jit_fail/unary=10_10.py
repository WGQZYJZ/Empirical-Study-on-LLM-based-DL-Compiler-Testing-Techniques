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

    def forward(self, x1):
        y1 = torch.clamp_min(torch.clamp_max(torch.nn.Linear(65056, 4096)(x1), 6.0), 0.0)
        y2 = torch.clamp_min(torch.clamp_max(torch.nn.Linear(4096, 4096)(y1), 6.0), 0.0)
        y3 = torch.clamp_min(torch.clamp_max(torch.nn.Linear(4096, 4096)(y2), 6.0), 0.0)
        y4 = torch.clamp_min(torch.clamp_max(torch.nn.Linear(4096, 4096)(y3), 6.0), 0.0)
        y5 = torch.clamp_min(torch.clamp_max(torch.nn.Linear(4096, 512)(y4), 6.0), 0.0)
        return y5



func = Model().to('cuda')



x1 = torch.randn(10, 65056)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cpu and cuda:0! (when checking argument for argument mat1 in method wrapper_CUDA_addmm)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., device='cuda:0', size=(10, 65056)), Parameter(FakeTensor(..., size=(4096, 65056), requires_grad=True)), Parameter(FakeTensor(..., size=(4096,), requires_grad=True))), **{}):
Unhandled FakeTensor Device Propagation for aten.mm.default, found two different devices cuda:0, cpu

from user code:
   File "<string>", line 18, in <resume in forward>
  File "/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/torch/nn/modules/module.py", line 1527, in _call_impl
    return forward_call(*args, **kwargs)
  File "/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/torch/nn/modules/linear.py", line 114, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''