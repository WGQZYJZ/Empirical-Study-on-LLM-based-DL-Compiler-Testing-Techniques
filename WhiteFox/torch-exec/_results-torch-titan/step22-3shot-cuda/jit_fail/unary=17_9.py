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
        self.module_0 = torch.nn.Flatten([2, 3])

    def forward(self, x1):
        v1 = self.module_0(x1)
        return v1




func = Model().to('cuda')



x1 = torch.randn(1, 4, 5, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
flatten() received an invalid combination of arguments - got (list, int), but expected one of:
 * (int start_dim, int end_dim, name out_dim)
 * (int start_dim, int end_dim)
      didn't match because some of the arguments have invalid types: (!list of [int, int]!, int)
 * (name start_dim, name end_dim, name out_dim)
 * (tuple of names dims, name out_dim)
      didn't match because some of the arguments have invalid types: (!list of [int, int]!, !int!)


jit:
Failed running call_module L__self___module_0(*(FakeTensor(..., device='cuda:0', size=(1, 4, 5, 2)),), **{}):
flatten() received an invalid combination of arguments - got (list, int), but expected one of:
 * (int start_dim, int end_dim, name out_dim)
 * (int start_dim, int end_dim)
      didn't match because some of the arguments have invalid types: (!list of [int, int]!, int)
 * (name start_dim, name end_dim, name out_dim)
 * (tuple of names dims, name out_dim)
      didn't match because some of the arguments have invalid types: (!list of [int, int]!, !int!)


from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''