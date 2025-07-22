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
        self.conv = torch.nn.Conv2d(512, 512, kernel_size=1, stride=1, padding=0, dilation=2)

    def forward(self, x):
        v1 = self.conv(x)
        v2 = torch.ops.quantized.linear(v1, ((3, 1), (1, 1)), 1, (0,), False)[:, 0]
        return v2




func = Model().to('cuda')



x = torch.randn(1, 512, 64, 64)


test_inputs = [x]

# JIT_FAIL
'''
direct:
quantized::linear() expected at most 4 argument(s) but received 5 argument(s). Declaration: quantized::linear(Tensor X, __torch__.torch.classes.quantized.LinearPackedParamsBase W_prepack, float Y_scale_i, int Y_zero_point_i) -> Tensor Y

jit:
Failed running call_function quantized.linear(*(FakeTensor(..., device='cuda:0', size=(1, 512, 64, 64)), ((3, 1), (1, 1)), 1, (0,), False), **{}):
quantized::linear() expected at most 4 argument(s) but received 5 argument(s). Declaration: quantized::linear(Tensor X, __torch__.torch.classes.quantized.LinearPackedParamsBase W_prepack, float Y_scale_i, int Y_zero_point_i) -> Tensor Y

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''