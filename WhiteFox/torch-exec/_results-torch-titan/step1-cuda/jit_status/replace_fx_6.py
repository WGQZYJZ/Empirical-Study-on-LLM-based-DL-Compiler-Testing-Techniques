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



class CustomLinearFunction(torch.autograd.Function):

    @staticmethod
    def forward(ctx, x1, x2, x3):
        ctx.save_for_backward(x1, x3)
        return ((x1 + x2) + x3)

    @staticmethod
    def backward(ctx, dy):
        (dx1, dx3) = ctx.saved_tensors
        return (dy, dy, dy)




class CustomModule(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 2)
        self.linear2 = torch.nn.Linear(2, 2)
        self.dropout = torch.nn.Dropout(p=0.5)
        self.custom_linear = CustomLinearFunction.apply

    def forward(self, x1):
        x1 = self.dropout(x1)
        x1 = self.dropout(x1)
        x2 = self.custom_linear(x1, self.linear1.weight, self.linear1.bias)
        x3 = torch.nn.functional.linear(x2, self.linear2.weight, self.linear2.bias)
        return x3



func = CustomModule().to('cuda')



dummy_input = torch.randn(1, 2, 2)


test_inputs = [dummy_input]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp0yrrafy0/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp0yrrafy0', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp0yrrafy0/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''