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
        self.conv = torch.nn.Conv2d(32, 64, kernel_size=(1, 1), stride=(1, 1), padding=(0, 0), dilation=(1, 1), groups=1, bias=True)
        nn.init.constant_(self.conv.weight.data, 0.11390784328985329)
        nn.init.constant_(self.conv.bias.data, 0.2092717409601135)

    def forward(self, x1):
        y = F.conv_transpose2d(x1, self.conv.weight, self.conv.bias, stride=None, padding=None, output_padding=1, groups=1, dilation=1, padding_mode='zeros', benchmark=True, deterministic=False)
        return y




func = Model().to('cuda')

x1 = 1

test_inputs = [x1]

# JIT_FAIL
'''
direct:
conv_transpose2d(): argument 'input' (position 1) must be Tensor, not int

jit:
Failed running call_function <built-in method conv_transpose2d of type object at 0x7672108699e0>(*(1, Parameter(FakeTensor(..., device='cuda:0', size=(64, 32, 1, 1), requires_grad=True)), Parameter(FakeTensor(..., device='cuda:0', size=(64,), requires_grad=True))), **{'stride': None, 'padding': None, 'output_padding': 1, 'groups': 1, 'dilation': 1, 'padding_mode': 'zeros', 'benchmark': True, 'deterministic': False}):
conv_transpose2d(): argument 'input' (position 1) must be Tensor, not int

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''