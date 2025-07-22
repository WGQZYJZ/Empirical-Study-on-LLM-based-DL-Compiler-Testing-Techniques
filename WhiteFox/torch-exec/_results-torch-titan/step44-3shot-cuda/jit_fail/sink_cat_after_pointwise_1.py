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
        x = x.view(x.shape[0], (- 1))
        x = torch.tanh(x)
        x = x.unsqueeze(dim=1)
        x = torch.cat([x, x, x], dim=(- 1))
        return torch.relu(x.flatten(begin_dim=1))




func = Model().to('cuda')



x = torch.randn(2, 3, 4)


test_inputs = [x]

# JIT_FAIL
'''
direct:
flatten() got an unexpected keyword argument 'begin_dim'

jit:
Failed running call_method flatten(*(FakeTensor(..., device='cuda:0', size=(2, 1, 36)),), **{'begin_dim': 1}):
flatten() got an unexpected keyword argument 'begin_dim'

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''