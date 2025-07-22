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
        p1 = torch.nn.functional.dropout(input=x1, p=0.4, train=False, inplace=False)
        x3 = torch.nn.functional.dropout(input=x1, p=0.6, train=False, inplace=False)
        x4 = x1.reshape(1, 4, 4)
        x4 = torch.nn.functional.dropout(input=x4, p=0.4, train=False, inplace=False)
        x5 = x1.reshape(1, 2, 2, 2)
        return x3




func = Model().to('cuda')



x1 = torch.randn(10)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
dropout() got an unexpected keyword argument 'train'

jit:
Failed running call_function <function dropout at 0x763313edf8b0>(*(), **{'input': FakeTensor(..., device='cuda:0', size=(10,)), 'p': 0.4, 'train': False, 'inplace': False}):
dropout() got an unexpected keyword argument 'train'

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''