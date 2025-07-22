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

    def forward(self, x1, x2):
        qk = ((x1 @ x2.transpose((- 2), (- 1))) / math.sqrt(x1.size((- 1))))
        qk = (qk + attn_mask)
        attn_weight = torch.softmax(qk, dim=(- 1))
        output = (x3 @ attn_weight)
        return output



func = Model().to('cuda')



x1 = torch.randn(4, 8, 32, 32)



x2 = torch.randn(4, 8, 32, 32)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
name 'attn_mask' is not defined

jit:
name 'attn_mask' is not defined

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''