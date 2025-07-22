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

    def forward(self, x1):
        x1 = x1.view(x1.shape[0], (- 1))
        x1 = x1.contiguous()
        x1 = x1.cat([x1, x1], dim=(- 1))
        x1 = torch.relu(x1)
        return x1




func = Model().to('cuda')



x1 = torch.randn(1, 2, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
'Tensor' object has no attribute 'cat'

jit:
Failed running call_method cat(*(FakeTensor(..., device='cuda:0', size=(1, 4)), [FakeTensor(..., device='cuda:0', size=(1, 4)), FakeTensor(..., device='cuda:0', size=(1, 4))]), **{'dim': -1}):
'FakeTensor' object has no attribute 'cat'

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''