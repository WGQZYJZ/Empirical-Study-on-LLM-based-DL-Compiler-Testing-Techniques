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
        self.conv_transpose2d1 = torch.nn.ConvTranspose2d(in_channels=2, out_channels=3, kernel_size=(3,), stride=(2,), padding=(1,))
        self.batch_norm2d1 = torch.nn.BatchNorm2d(num_features=3)
        self.linear3 = torch.nn.Linear(in_features=9, out_features=20)

    def forward(self, x0, x1):
        x0 = self.conv_transpose2d1(x0)
        x1 = self.batch_norm2d1(x1)
        y0 = x1.transpose()
        y1 = x0.view(x0.size())
        y2 = y1 + x1
        y3 = y1.neg()
        y4 = y0 + y3
        y5 = y0 + y2
        y6 = y4 + x1.transpose()
        y7 = x1 + y6
        y8 = self.linear3(y5)
        return (y5, y7, y8)



func = Model().to('cpu')


input1 = torch.randn(4, 2, 8, 8)

input2 = torch.randn(4, 3, 4, 4)

test_inputs = [input1, input2]

# JIT_FAIL
'''
direct:
expected dilation to be a single integer value or a list of 1 values to match the convolution dimensions, but got dilation=[1, 1]

jit:
Failed running call_function <built-in method conv_transpose2d of type object at 0x7bc74ef96ec0>(*(FakeTensor(..., size=(4, 2, 8, 8)), Parameter(FakeTensor(..., size=(2, 3, 3), requires_grad=True)), Parameter(FakeTensor(..., size=(3,), requires_grad=True)), (2,), (1,), (0, 0), 1, (1, 1)), **{}):
tuple index out of range

from user code:
   File "<string>", line 22, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 1162, in forward
    return F.conv_transpose2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''