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
        a1 = torch.add(x1, x1)
        a2 = torch.dropout(input=a1, p=0.0, training=True)
        a3 = torch.mul(a1, a1)
        return torch.add(a2, a3)




func = Model().to('cuda')



x1 = torch.randn(16, 8)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
dropout() missing 1 required positional arguments: "train"

jit:
Failed running call_function <built-in method dropout of type object at 0x736b320699e0>(*(), **{'input': FakeTensor(..., device='cuda:0', size=(16, 8)), 'p': 0.0, 'training': True}):
dropout() missing 1 required positional arguments: "train"

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''