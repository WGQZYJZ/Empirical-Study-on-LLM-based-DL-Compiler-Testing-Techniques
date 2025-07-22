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
        self.m1 = torch.nn.Unfold(kernel_size=(3, 9), stride=(2, 8), padding=(0, 7), dilation=(2, 1))
        self.m2 = torch.nn.Fold((4, 10), kernel_size=(3, 9), stride=(2, 8), padding=(0, 7), dilation=(2, 1))

    def forward(self, x):
        return self.m2(self.m1(x))




func = Model().to('cuda')



x = torch.randn(20, 16, 6, 9)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Given output_size=(4, 10), kernel_size=(3, 9), dilation=(2, 1), padding=(0, 7), stride=(2, 8), expected size of input's dimension 2 to match the calculated number of sliding blocks 0 * 2 = 0, but got input.size(2)=2.

jit:
Failed running call_module L__self___m2(*(FakeTensor(..., device='cuda:0', size=(20, 432, 2)),), **{}):
Given output_size=[4, 10], kernel_size=[3, 9], dilation=[2, 1], padding=[0, 7], stride=[2, 8], expected input.size(-1) to be 0 but got 2.

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''