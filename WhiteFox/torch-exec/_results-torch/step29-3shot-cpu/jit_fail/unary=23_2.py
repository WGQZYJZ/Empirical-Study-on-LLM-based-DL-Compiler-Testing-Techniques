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
        self.conv_transpose1 = torch.nn.ConvTranspose2d(3, 3, (2, 5), stride=(1, 3), padding=(1, 1))
        self.conv_transpose2 = torch.nn.ConvTranspose2d(3, 4, (4, 2), stride=(4, 1), padding=(2, 2))
        self.conv_transpose3 = torch.nn.ConvTranspose2d(5, 6, kernel_size=1, stride=1, padding=0)

    def forward(self, x):
        x = self.conv_transpose1(x)
        x = self.conv_transpose2(x)
        x = self.conv_transpose3(x)
        return x



func = MyModule().to('cpu')


x = torch.randn(1, 3, 5, 7)

test_inputs = [x]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [5, 6, 1, 1], expected input[1, 4, 12, 18] to have 5 channels, but got 4 channels instead

jit:
Failed running call_function <built-in method conv_transpose2d of type object at 0x7813b4f96ec0>(*(FakeTensor(..., size=(1, 4, 12, 18)), Parameter(FakeTensor(..., size=(5, 6, 1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(6,), requires_grad=True)), (1, 1), (0, 0), (0, 0), 1, (1, 1)), **{}):
Given transposed=1, weight of size [5, 6, 1, 1], expected input[1, 4, 12, 18] to have 5 channels, but got 4 channels instead

from user code:
   File "<string>", line 24, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 1162, in forward
    return F.conv_transpose2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''