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



class Model(nn.Module):

    def __init__(self):
        super().__init__()
        self.layers = nn.Linear(100, 10)

    def forward(self, x):
        x = self.layers(x)
        x = x.softmax(dim=(- 1))
        f = x[:, 3].unsqueeze((- 1))
        e = x[:, 4].unsqueeze((- 1))
        x = x.gather(dim=(- 1), index=f)
        x = (x / e)
        x = x.log()
        return x




func = Model().to('cuda')



x = torch.randn(5, 100)


test_inputs = [x]

# JIT_FAIL
'''
direct:
gather(): Expected dtype int64 for index

jit:
Failed running call_method gather(*(FakeTensor(..., device='cuda:0', size=(5, 10)),), **{'dim': -1, 'index': FakeTensor(..., device='cuda:0', size=(5, 1))}):
gather(): Expected dtype int64 for index, but got torch.float32

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''