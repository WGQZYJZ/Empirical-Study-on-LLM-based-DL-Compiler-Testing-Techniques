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

    def forward(self, input1, input2):
        v = []
        v.append(torch.mm(input1, input2))
        v.append(torch.mm(input1, input2))
        v.append(torch.squeeze(torch.t(torch.squeeze(torch.t(input1)), 1), 2))
        return torch.cat(v, 2)




func = Model().to('cuda')



input1 = torch.randn(2, 2)



input2 = torch.randn(2, 1)


test_inputs = [input1, input2]

# JIT_FAIL
'''
direct:
t() takes 1 positional argument but 2 were given

jit:
Failed running call_function <built-in method t of type object at 0x709cf3a699e0>(*(FakeTensor(..., device='cuda:0', size=(2, 2)), 1), **{}):
t() takes 1 positional argument but 2 were given

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''