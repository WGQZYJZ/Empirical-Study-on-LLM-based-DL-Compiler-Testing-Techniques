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



class ScaledDotProductAttention(nn.Module):

    def __init__(self, d_key: int, d_value: int, d_model: int):
        super().__init__()
        self.scale = torch.sqrt(torch.FloatTensor([d_key]))
        self.d_key = d_key

    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor) -> torch.Tensor:
        x = torch.matmul(query, key.transpose((- 2), (- 1)))
        x = (x / self.scale)
        x = F.softmax(x, dim=(- 1))
        y = torch.matmul(x, value)
        return y




class Model(nn.Module):

    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.attention = ScaledDotProductAttention(8, 8, 8)

    def forward(self, x1: torch.Tensor) -> torch.Tensor:
        x2 = self.conv(x1)
        y = self.attention(x2, x2, x2)
        return y



func = Model().to('cuda')



x1 = torch.randn(8, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu!

jit:
Failed running call_function <built-in function truediv>(*(FakeTensor(..., device='cuda:0', size=(8, 8, 66, 66)), FakeTensor(..., size=(1,))), **{}):
Unhandled FakeTensor Device Propagation for aten.div.Tensor, found two different devices cuda:0, cpu

from user code:
   File "<string>", line 41, in forward
  File "/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/torch/nn/modules/module.py", line 1527, in _call_impl
    return forward_call(*args, **kwargs)
  File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''