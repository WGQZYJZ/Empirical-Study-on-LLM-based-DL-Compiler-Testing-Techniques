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
        self.softmax = torch.nn.Softmax2d()

    def forward(self, x6):
        v1 = self.softmax(x6)
        v6 = torch.clamp_max(v1, max_value)
        return v6



func = Model().to('cpu')

x6 = 1

test_inputs = [x6]

# JIT_FAIL
'''
direct:
'int' object has no attribute 'dim'

jit:
AttributeError: 'int' object has no attribute 'dim'

from user code:
   File "<string>", line 20, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/activation.py", line 1701, in forward
    if input.dim() not in (3, 4):


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''