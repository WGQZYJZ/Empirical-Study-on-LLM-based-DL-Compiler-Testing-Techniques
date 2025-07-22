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

    def forward(self, x):
        y1 = x.add(x)
        y2 = torch.cat((y1, x), dim=1).view(y1.shape[0], (- 1)).tanh()
        y3 = torch.cat((y1, y2), dim=1).view(y1.shape[0], (- 1)).tanh()
        return y3




func = Model().to('cuda')



x = torch.randn(3, 3, 4)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Tensors must have same number of dimensions: got 3 and 2

jit:
backend='inductor' raised:
LoweringException: AssertionError: 
  target: aten.cat.default
  args[0]: [TensorBox(StorageBox(
    Pointwise(
      'cuda',
      torch.float32,
      def inner_fn(index):
          i0, i1, i2 = index
          tmp0 = ops.load(arg0_1, i2 + 4 * i1 + 12 * i0)
          tmp1 = ops.load(arg0_1, i2 + 4 * i1 + 12 * i0)
          tmp2 = tmp0 + tmp1
          tmp3 = ops.tanh(tmp2)
          return tmp3
      ,
      ranges=[3, 3, 4],
      origin_node=tanh_2,
      origins={add, tanh_2}
    )
  )), TensorBox(StorageBox(
    Pointwise(
      'cuda',
      torch.float32,
      def inner_fn(index):
          i0, i1 = index
          tmp0 = ops.load(buf2, i1 + 24 * i0)
          tmp1 = ops.tanh(tmp0)
          return tmp1
      ,
      ranges=[3, 24],
      origin_node=tanh_3,
      origins={tanh_3}
    )
  ))]
  args[1]: 1


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''