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
        qk = (qk + qm)
        attn_weight = torch.softmax(qk, dim=(- 1))
        attn_weight = torch.dropout(attn_weight, dropout_p, True)
        output = (attn_weight @ x2)
        return output



func = Model().to('cuda')



x1 = torch.randn(4, 3, 64)



x2 = torch.randn(4, 5, 64)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
name 'qm' is not defined

jit:
name 'qm' is not defined

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''