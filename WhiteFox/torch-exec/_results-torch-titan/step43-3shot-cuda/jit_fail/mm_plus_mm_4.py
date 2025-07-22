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



class TestModel(torch.nn.Module):

    def forward(self, x):
        x = torch.mm(self.a, x)
        x = torch.mm(self.b, x)
        c = torch.mm(self.c, x)
        x = (x + c)
        x = (c + x)
        x = (x + c)
        x = (c + x)
        x = self.relu(x)
        x = self.relu(self.relu(self.relu(self.relu(x))))
        res = (x * x)
        return res




func = TestModel().to('cuda')



input = torch.randn(4, 4)


test_inputs = [input]

# JIT_FAIL
'''
direct:
'TestModel' object has no attribute 'a'

jit:
a

from user code:
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''