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
        y = y.view(y.shape[0], (- 1))
        x = y.view(y.shape[0], (- 1))
        y = x.view(y.shape[0], (- 1)).relu()
        x = y.view((- 1), y.shape[1]).relu()
        y = x.view(y.type(torch.BoolTensor))
        return x




func = Model().to('cuda')



x = torch.randn(2, 3, 4)


test_inputs = [x]

# JIT_FAIL
'''
direct:
view() received an invalid combination of arguments - got (Tensor), but expected one of:
 * (torch.dtype dtype)
      didn't match because some of the arguments have invalid types: (!Tensor!)
 * (tuple of ints size)
      didn't match because some of the arguments have invalid types: (!Tensor!)


jit:
Failed running call_method view(*(FakeTensor(..., device='cuda:0', size=(2, 12)), FakeTensor(..., size=(2, 12), dtype=torch.bool)), **{}):
view() received an invalid combination of arguments - got (FakeTensor), but expected one of:
 * (torch.dtype dtype)
      didn't match because some of the arguments have invalid types: (!FakeTensor!)
 * (tuple of ints size)
      didn't match because some of the arguments have invalid types: (!FakeTensor!)


from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''