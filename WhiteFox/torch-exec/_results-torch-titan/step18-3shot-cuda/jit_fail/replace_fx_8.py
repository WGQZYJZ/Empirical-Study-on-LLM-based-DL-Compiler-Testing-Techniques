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



class model(torch.nn.Module):

    def __init__(self):
        super(model, self).__init__()
        self.a = torch.rand(5)
        self.b = torch.rand(5)

    def forward(self, input):
        y1 = torch.rand_like(input)
        y3 = torch.add(input, y1)
        y2 = torch.dropout(self.a)
        y4 = torch.rand_like(input)
        y = torch.add(y3, y4)
        return y




func = model().to('cuda')



input1 = torch.zeros(5)


test_inputs = [input1]

# JIT_FAIL
'''
direct:
dropout() missing 2 required positional argument: "p", "train"

jit:
Failed running call_function <built-in method dropout of type object at 0x751f8ba699e0>(*(FakeTensor(..., device='cuda:0', size=(5,)),), **{}):
dropout() missing 2 required positional argument: "p", "train"

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''