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
        x2 = torch.zeros_like(x1, dtype=torch.float, device=(torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')))
        x3 = torch.rand_like(x1, dtype=torch.float, device=(torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')))
        x4 = torch.rand_like(x1, dtype=torch.float, device=(torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')))




func = Model().to('cuda')

x1 = 1

test_inputs = [x1]

# JIT_FAIL
'''
direct:
zeros_like(): argument 'input' (position 1) must be Tensor, not int

jit:
Failed running call_function <built-in method zeros_like of type object at 0x739ff50699e0>(*(1,), **{'dtype': torch.float32, 'device': device(type='cuda')}):
zeros_like(): argument 'input' (position 1) must be Tensor, not int

from user code:
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''