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
        v1 = torch.transpose(x1, 0, 1)
        v2 = torch.transpose(v1, 1, 2)
        v3 = torch.transpose(v2, 0, 1)
        v4 = torch.transpose(v3, 2, 3)
        v5 = torch.reshape(v4, (4, 384))
        v6 = torch.reshape(v5, (4, 27, 4, 16))
        return v6




func = Model().to('cuda')





x1 = torch.reshape(torch.arange((((4 * 27) * 4) * 16), dtype=torch.float32), (4, 1, 27, 4, 16))


test_inputs = [x1]

# JIT_FAIL
'''
direct:
shape '[4, 384]' is invalid for input of size 6912

jit:
Failed running call_function <built-in method reshape of type object at 0x7b42230699e0>(*(FakeTensor(..., device='cuda:0', size=(27, 1, 4, 4, 16)), (4, 384)), **{}):
shape '[4, 384]' is invalid for input of size 6912

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''