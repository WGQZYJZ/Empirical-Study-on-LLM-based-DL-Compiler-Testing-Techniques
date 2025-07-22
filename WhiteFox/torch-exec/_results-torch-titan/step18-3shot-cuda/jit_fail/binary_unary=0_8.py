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



class M1(torch.nn.Module):

    def __init__(self):
        super().__init__()

    def forward(self, x, **kwargs):
        t = (x + kwargs['key'])
        return t




class M2(M1):
    pass




class M3(M2):
    pass




class M4(M3):
    pass




func = M4().to('cuda')



x = torch.randn(1, 16, 64, 64)


test_inputs = [x]

# JIT_FAIL
'''
direct:
'key'

jit:
key

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''