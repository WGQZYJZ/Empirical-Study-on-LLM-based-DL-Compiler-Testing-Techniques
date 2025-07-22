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
        x = F.conv2d(x, torch.rand(3, 3, 3, 3), stride=1)
        x = F.batch_norm(x, num_features=3)
        return x




func = Model().to('cuda')



x = torch.randn(1, 3, 6, 6)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Input type (torch.cuda.FloatTensor) and weight type (torch.FloatTensor) should be the same

jit:
Failed running call_function <function batch_norm at 0x77db3ada1b80>(*(FakeTensor(..., device='cuda:0', size=(1, 3, 4, 4)),), **{'num_features': 3}):
batch_norm() got an unexpected keyword argument 'num_features'

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''