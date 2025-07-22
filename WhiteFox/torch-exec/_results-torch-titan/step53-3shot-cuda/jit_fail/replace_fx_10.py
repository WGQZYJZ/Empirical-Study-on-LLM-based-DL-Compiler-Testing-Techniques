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

    def forward(self, x):
        x = F.dropout(x, p=0.5)
        x = F.dropout(x, p=0)
        return x




func = model().to('cuda')

x = 1

test_inputs = [x]

# JIT_FAIL
'''
direct:
dropout(): argument 'input' (position 1) must be Tensor, not int

jit:
Failed running call_function <function dropout at 0x771b0fe1f8b0>(*(1,), **{'p': 0.5}):
dropout(): argument 'input' (position 1) must be Tensor, not int

from user code:
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''