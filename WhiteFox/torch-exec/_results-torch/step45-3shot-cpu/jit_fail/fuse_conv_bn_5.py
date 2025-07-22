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
        torch.manual_seed(1)
        self.conv1 = torch.nn.Conv1d(1, 1, 1)
        self.conv3 = torch.nn.Conv3d(1, 1, 1)

    def forward(self, x):
        return self.conv1(x) + self.conv3(x)



func = Model().to('cpu')


x1 = torch.randn(1, 1, 32)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected 4D (unbatched) or 5D (batched) input to conv3d, but got input of size: [1, 1, 32]

jit:
Failed running call_function <built-in method conv3d of type object at 0x767573996ec0>(*(FakeTensor(..., size=(1, 1, 32)), Parameter(FakeTensor(..., size=(1, 1, 1, 1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(1,), requires_grad=True)), (1, 1, 1), (0, 0, 0), (1, 1, 1), 1), **{}):
Expected 4D (unbatched) or 5D (batched) input to conv3d, but got input of size: [1, 1, 32]

from user code:
   File "<string>", line 22, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 725, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 720, in _conv_forward
    return F.conv3d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''