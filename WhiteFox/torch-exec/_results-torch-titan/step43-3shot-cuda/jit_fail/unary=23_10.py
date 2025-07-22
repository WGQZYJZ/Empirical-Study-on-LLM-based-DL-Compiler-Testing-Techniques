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
        self.conv_transpose_a = torch.nn.ConvTranspose2d(16, 1, kernel_size=3, stride=1, padding=1, output_padding=1)
        self.conv_transpose_b = torch.nn.ConvTranspose2d(16, 12, 3, stride=2, padding=1)

    def forward(self, x1):
        v1 = self.conv_transpose_a(x1)
        v2 = self.conv_transpose_b(x1)
        v3 = torch.tanh(v1)
        v4 = torch.tanh(v2)
        v5 = (v3 + v4)
        return (v1, v5)




func = Model().to('cuda')



x1 = torch.randn(1, 16, 26, 26)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
output padding must be smaller than either stride or dilation, but got output_padding_height: 1 output_padding_width: 1 stride_height: 1 stride_width: 1 dilation_height: 1 dilation_width: 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 1, 27, 27)), FakeTensor(..., device='cuda:0', size=(1, 12, 51, 51))), **{}):
Attempting to broadcast a dimension of length 51 at -1! Mismatching argument at index 1 had torch.Size([1, 12, 51, 51]); but expected shape should be broadcastable to [1, 1, 27, 27]

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''