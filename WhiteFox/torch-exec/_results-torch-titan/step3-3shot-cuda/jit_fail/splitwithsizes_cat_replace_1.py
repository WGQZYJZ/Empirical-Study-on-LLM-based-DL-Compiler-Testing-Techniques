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
        v1 = (x1 + torch.split(input=x1, split_size_or_sections=[1, 2], dim=1))
        v2 = torch.cat([v1[0], v1[2]], dim=1)
        return torch.split(input=v2, split_size_or_sections=[1, 2], dim=1)



func = Model().to('cuda')



x1 = torch.randn(size=[1, 3, 64, 64])


test_inputs = [x1]

# JIT_FAIL
'''
direct:
split() got an unexpected keyword argument 'input'

jit:
Failed running call_function <function split at 0x756e80b2f0d0>(*(), **{'input': FakeTensor(..., device='cuda:0', size=(1, 3, 64, 64)), 'split_size_or_sections': [1, 2], 'dim': 1}):
split() got an unexpected keyword argument 'input'

from user code:
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''