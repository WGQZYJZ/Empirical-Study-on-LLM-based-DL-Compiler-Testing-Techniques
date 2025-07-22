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

    def forward(self, q4, q5, k3, v4, mask):
        qk = ((q3 @ k2.transpose((- 2), (- 1))) / math.sqrt(q3.size((- 1))))
        qk = (qk + mask)
        attn_weight = torch.softmax(qk, dim=(- 1))
        output = (attn_weight @ v2)
        return output




func = Model().to('cuda')

q4 = 1
q5 = 1
k3 = 1
v4 = 1
mask = 1

test_inputs = [q4, q5, k3, v4, mask]

# JIT_FAIL
'''
direct:
name 'q3' is not defined

jit:
name 'q3' is not defined

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''