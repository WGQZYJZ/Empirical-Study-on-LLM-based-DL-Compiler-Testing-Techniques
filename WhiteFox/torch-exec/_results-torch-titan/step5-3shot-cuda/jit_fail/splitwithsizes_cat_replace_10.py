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
        self.split0 = torch.nn.Conv2d(3, 1, 3, stride=1, padding=1)
        self.split1 = torch.nn.Conv2d(3, 1, 3, stride=1, padding=1)
        self.split2 = torch.nn.Conv2d(1, 1, 3, stride=1, padding=1)

    def forward(self, input_tensor, split_size):
        split = torch.split(input_tensor, split_size)
        out = (split[0] + self.split0(split[1]))
        out = ((out + self.split1(split[2])) + self.split2(split[3]))
        out = torch.cat(out)
        return out



func = Model().to('cuda')



split_size = torch.tensor([9, 9, 9, 9])

input_tensor = 1

test_inputs = [split_size, input_tensor]

# JIT_FAIL
'''
direct:
Input type (long int) and bias type (float) should be the same

jit:
Failed running call_module L__self___split0(*(FakeTensor(..., device='cuda:0', size=(1,), dtype=torch.int64),), **{}):
Input type (long int) and bias type (float) should be the same

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''