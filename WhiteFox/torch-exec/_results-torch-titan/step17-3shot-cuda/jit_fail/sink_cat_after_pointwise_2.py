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
        y[:, :3] = (- y[:, :3])
        y = y.relu().tanh()
        y = torch.cat((x, y), dim=1)
        z = torch.tanh(torch.tanh(y))
        return z




func = Model().to('cuda')



x = torch.randn(2, 3, 4)


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
          tmp0 = ops.index_expr(i2 + 4 * i1, torch.int64)
          tmp1 = ops.index_expr(3, torch.int64)
          tmp2 = tmp0 < tmp1
          tmp3 = ops.load(arg0_1, i2 + 4 * i1 + 12 * i0)
          tmp4 = -tmp3
          tmp5 = ops.masked(tmp2, tmp4, 0.0)
          tmp6 = ops.load(arg0_1, i2 + 4 * i1 + 12 * i0)
          tmp7 = ops.where(tmp2, tmp5, tmp6)
          tmp8 = ops.tanh(tmp7)
          return tmp8
      ,
      ranges=[2, 3, 4],
      origin_node=tanh_1,
      origins={tanh_1}
    )
  )), TensorBox(StorageBox(
    Pointwise(
      'cuda',
      torch.float32,
      def inner_fn(index):
          i0, i1 = index
          tmp0 = ops.index_expr(4 * ModularIndexing(i1, 4, 3) + ModularIndexing(i1, 1, 4), torch.int64)
          tmp1 = ops.index_expr(3, torch.int64)
          tmp2 = tmp0 < tmp1
          tmp3 = ops.load(arg0_1, 4 * ModularIndexing(i1, 4, 3) + 12 * i0 + ModularIndexing(i1, 1, 4))
          tmp4 = -tmp3
          tmp5 = ops.masked(tmp2, tmp4, 0.0)
          tmp6 = ops.load(arg0_1, 4 * ModularIndexing(i1, 4, 3) + 12 * i0 + ModularIndexing(i1, 1, 4))
          tmp7 = ops.where(tmp2, tmp5, tmp6)
          tmp8 = ops.relu(tmp7)
          tmp9 = ops.tanh(tmp8)
          tmp10 = ops.tanh(tmp9)
          return tmp10
      ,
      ranges=[2, 12],
      origin_node=tanh_2,
      origins={tanh_2, relu, tanh}
    )
  ))]
  args[1]: 1


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''