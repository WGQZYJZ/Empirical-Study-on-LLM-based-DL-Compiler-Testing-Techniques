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
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1, x2, x3, x4):
        v1 = torch.nn.functional.linear(x1, self.linear.weight, self.linear.bias)
        v2 = v1.permute(0, 1, 3, 2)
        v3 = torch.nn.functional.linear(x2, self.linear.weight, self.linear.bias)
        v4 = v3.permute(0, 2, 3, 1)
        v5 = torch.nn.functional.linear(x3, self.linear.weight, self.linear.bias)
        v6 = torch.nn.functional.linear(x4, self.linear.weight, self.linear.bias)
        v7 = v6.permute(0, 1, 3, 2)
        v8 = torch.nn.functional.linear(x4, self.linear.weight, self.linear.bias)
        v9 = v8.permute(0, 2, 1, 3)
        return (((v2 + v4) + v7) + v9)




func = Model().to('cuda')



x1 = torch.randn(1, 2, 2, 2, device='cpu')



x2 = torch.randn(1, 2, 2, 2, device='cpu')



x3 = torch.randn(1, 2, 2, 2, device='cpu')



x4 = torch.randn(1, 2, 2, 2, device='cpu')


test_inputs = [x1, x2, x3, x4]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpfqe0cka5/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpfqe0cka5', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpfqe0cka5/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''