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
        y = x.view(x.shape[0], (- 1))
        y = y.view(y.shape[0], (- 1)).tanh()
        (x1, x2) = torch.chunk(y, 2, dim=0)
        y = torch.cat((x1, x2), dim=1)
        y = y.view((- 1)).tanh()
        x = x.tan()
        y = y.view((- 1)).tanh()
        x = torch.cat((x, y), dim=0)
        x = x.tanh()
        x = x.tanh()
        return x




func = Model().to('cuda')



x = torch.randn(6, 3, 4)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Tensors must have same number of dimensions: got 3 and 1

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
          tmp1 = ops.tan(tmp0)
          tmp2 = ops.tanh(tmp1)
          return tmp2
      ,
      ranges=[6, 3, 4],
      origin_node=tanh_4,
      origins={tan, tanh_4}
    )
  )), TensorBox(StorageBox(
    Pointwise(
      'cuda',
      torch.float32,
      def inner_fn(index):
          i0 = index
          tmp0 = ops.load(buf2, i0)
          tmp1 = ops.tanh(tmp0)
          tmp2 = ops.tanh(tmp1)
          return tmp2
      ,
      ranges=[72],
      origin_node=tanh_5,
      origins={tanh_5, tanh_3}
    )
  ))]


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''