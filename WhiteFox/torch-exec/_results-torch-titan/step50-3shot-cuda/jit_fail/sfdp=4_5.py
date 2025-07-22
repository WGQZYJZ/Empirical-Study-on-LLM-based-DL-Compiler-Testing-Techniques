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

    def forward(self, Q):
        Q3 = nn.Conv2d(Q.shape[1], Q.shape[1], (1, 1))
        Q3.weight = torch.nn.Parameter(torch.tensor([]))
        k = torch.randn(Q.shape[1], Q.shape[1], 1, 1)
        v = Q
        mask = (torch.rand(1, 56, 56) > 0.7).fill_((- 1000000000.0))
        qk = ((Q3(Q) @ k.transpose((- 2), (- 1))) / math.sqrt(Q.size((- 1))))
        qk = (qk + mask)
        attn_weight = torch.softmax(qk, dim=(- 1))
        output = (attn_weight @ v)
        return output




func = Model().to('cuda')



Q = torch.randn(1, 64, 56, 56)


test_inputs = [Q]

# JIT_FAIL
'''
direct:
weight should have at least three dimensions

jit:
Failed running call_function <built-in method conv2d of type object at 0x7a098be699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 64, 56, 56)), Parameter(FakeTensor(..., size=(0,), requires_grad=True)), Parameter(FakeTensor(..., size=(64,), requires_grad=True)), (1, 1), (0, 0), (1, 1), 1), **{}):
expected stride to be a single integer value or a list of -1 values to match the convolution dimensions, but got stride=[1, 1]

from user code:
   File "<string>", line 26, in <resume in forward>
  File "/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/torch/nn/modules/module.py", line 1527, in _call_impl
    return forward_call(*args, **kwargs)
  File "/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/torch/nn/modules/conv.py", line 460, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/torch/nn/modules/conv.py", line 456, in _conv_forward
    return F.conv2d(input, weight, bias, self.stride,


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''