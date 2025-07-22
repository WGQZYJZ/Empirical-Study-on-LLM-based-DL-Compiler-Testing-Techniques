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



class MyModule(torch.nn.Module):

    def __init__(self):
        super(MyModule, self).__init__()

    def forward(self, x):
        if ((x.shape[1] == 0) or (x.shape[1] == 3) or (x.shape[1] == 5)):
            return x
        if hasattr(torch.nn.functional, 'max_pool1d'):
            return torch.nn.functional.max_pool1d(x, 2, 2)
        else:
            return torch.max_pool1d(x, 2, 2)




class Model(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 3, 2)
        self.pool2d = MyModule()
        self.conv2 = torch.nn.Conv2d(3, 3, 2, padding=(3, 1), dilation=(3, 2))

    def forward(self, x):
        x = self.conv(x)
        x = self.pool2d(x)
        x = self.conv2(x)
        return x




func = Model().to('cuda')



x = torch.randint(0, 100, (1, 3, 10, 10))


test_inputs = [x]

# JIT_FAIL
'''
direct:
Input type (long int) and bias type (float) should be the same

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(1, 3, 10, 10), dtype=torch.int64),), **{}):
Input type (long int) and bias type (float) should be the same

from user code:
   File "<string>", line 40, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''