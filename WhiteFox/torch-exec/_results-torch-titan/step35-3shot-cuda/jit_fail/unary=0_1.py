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
        self.conv2d_0 = torch.nn.Conv2d(4, 2, (1, 3), stride=(2, 1), padding=[[0, 0], [1, 1]])
        self.conv2d_1 = torch.nn.Conv2d(4, 6, 2, stride=(3, 1), padding=1)

    def forward(self, x1):
        v1 = self.conv2d_0(x1)
        v2 = self.conv2d_1(x1)
        v3 = self.conv2d_0(v1)
        v4 = self.conv2d_0(v2)
        v5 = self.conv2d_0(v3)
        v6 = self.conv2d_0(v4)
        v7 = self.conv2d_1(v5)
        v8 = self.conv2d_0(v7)
        v9 = self.conv2d_0(v8)
        v10 = (v5 * 0.044715)
        v11 = (v6 + v10)
        v12 = (v11 * 0.7978845608028654)
        v13 = torch.tanh(v12)
        v14 = (v13 + 1)
        v15 = (v14 * 0.5)
        v16 = (v14 * v14)
        v17 = (v17 * v14)
        v18 = (v18 * 0.044715)
        v19 = (v16 + v18)
        v20 = (v19 * 0.7978845608028654)
        v21 = torch.tanh(v20)
        v22 = (v21 + 1)
        v23 = (v15 * v22)
        v24 = (v17 * v22)
        v25 = (v24 * 0.044715)
        v26 = (v23 + v25)
        return torch.cat((v26, v23, v26), 1)




func = Model().to('cuda')



x1 = torch.randn(1, 4, 40)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
conv2d() received an invalid combination of arguments - got (Tensor, Parameter, Parameter, tuple, tuple, tuple, int), but expected one of:
 * (Tensor input, Tensor weight, Tensor bias, tuple of ints stride, tuple of ints padding, tuple of ints dilation, int groups)
      didn't match because some of the arguments have invalid types: (Tensor, !Parameter!, !Parameter!, !tuple of (int, int)!, !tuple of (list, list)!, !tuple of (int, int)!, int)
 * (Tensor input, Tensor weight, Tensor bias, tuple of ints stride, str padding, tuple of ints dilation, int groups)
      didn't match because some of the arguments have invalid types: (Tensor, !Parameter!, !Parameter!, !tuple of (int, int)!, !tuple of (list, list)!, !tuple of (int, int)!, int)


jit:
Failed running call_module L__self___conv2d_0(*(FakeTensor(..., device='cuda:0', size=(1, 4, 40)),), **{}):
conv2d() received an invalid combination of arguments - got (FakeTensor, FakeTensor, FakeTensor, tuple, tuple, tuple, int), but expected one of:
 * (Tensor input, Tensor weight, Tensor bias, tuple of ints stride, tuple of ints padding, tuple of ints dilation, int groups)
      didn't match because some of the arguments have invalid types: (!FakeTensor!, !FakeTensor!, !FakeTensor!, !tuple of (int, int)!, !tuple of (list, list)!, !tuple of (int, int)!, int)
 * (Tensor input, Tensor weight, Tensor bias, tuple of ints stride, str padding, tuple of ints dilation, int groups)
      didn't match because some of the arguments have invalid types: (!FakeTensor!, !FakeTensor!, !FakeTensor!, !tuple of (int, int)!, !tuple of (list, list)!, !tuple of (int, int)!, int)


from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''