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



class model(torch.nn.Module):

    def __init__(self):
        super().__init__()

    def forward(self, x1, x2, x3):
        a = torch.nn.functional.dropout(x1, p=0.1)
        b = F.dropout2d(x2, p=0.3, training=None)
        c = torch.nn.functional.dropout(b, p=0.5)
        d = torch.nn.functional.dropout(x3, p=0.6, training=False)
        return (c + d)




func = model().to('cuda')



x1 = torch.randn(3, 8, 8)



x2 = torch.randn(3, 20, 20)



x3 = torch.randn(3, 30, 30)


test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
feature_dropout(): argument 'train' (position 3) must be bool, not NoneType

jit:
Failed running call_function <function dropout2d at 0x7ba90d9dda60>(*(FakeTensor(..., device='cuda:0', size=(3, 20, 20)),), **{'p': 0.3, 'training': None}):
feature_dropout(): argument 'train' (position 3) must be bool, not NoneType

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''