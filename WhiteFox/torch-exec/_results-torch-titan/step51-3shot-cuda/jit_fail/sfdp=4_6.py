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

    def forward(self, input1, input2, input3, input4):
        qk = ((input1 @ input2.transpose((- 2), (- 1))) / math.sqrt(input1.size((- 1))))
        qk = (qk + input4)
        attn_weight = torch.softmax(qk, dim=(- 1))
        output = (attn_weight @ input3)
        return output




func = Model().to('cuda')

input1 = 1
input2 = 1
input3 = 1
input4 = 1

test_inputs = [input1, input2, input3, input4]

# JIT_FAIL
'''
direct:
'int' object has no attribute 'transpose'

jit:
'int' object has no attribute 'transpose'

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''