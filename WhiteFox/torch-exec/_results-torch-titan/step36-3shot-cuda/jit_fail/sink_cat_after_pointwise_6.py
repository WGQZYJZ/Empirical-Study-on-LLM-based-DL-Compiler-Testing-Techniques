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



class SinkCatInput(torch.nn.Module):

    def __init__(self):
        super().__init__()

    def forward(self, x):
        x = torch.cat((torch.squeeze(x), x), dim=0).view(x.shape[0], (- 1))
        x = torch.tanh(x)
        return x




func = SinkCatInput().to('cuda')



x = torch.randn(3, 1)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Tensors must have same number of dimensions: got 1 and 2

jit:
backend='inductor' raised:
LoweringException: AssertionError: 
  target: aten.cat.default
  args[0]: [TensorBox(StorageBox(
    Pointwise(
      'cuda',
      torch.float32,
      def inner_fn(index):
          i0 = index
          tmp0 = ops.load(arg0_1, i0)
          tmp1 = ops.tanh(tmp0)
          return tmp1
      ,
      ranges=[3],
      origin_node=tanh,
      origins={tanh}
    )
  )), TensorBox(StorageBox(
    Pointwise(
      'cuda',
      torch.float32,
      def inner_fn(index):
          i0, _ = index
          tmp0 = ops.load(arg0_1, i0)
          tmp1 = ops.tanh(tmp0)
          return tmp1
      ,
      ranges=[3, 1],
      origin_node=tanh_1,
      origins={tanh_1}
    )
  ))]


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''