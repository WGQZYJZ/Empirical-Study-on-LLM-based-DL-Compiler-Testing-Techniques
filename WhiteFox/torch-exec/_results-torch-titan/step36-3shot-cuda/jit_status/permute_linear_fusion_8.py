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

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        x2 = torch.nn.functional.tanhshrink(v2)
        v3 = x2.detach()
        v4 = torch.max(v3, dim=(- 1))[1]
        v4 = v4.unsqueeze(dim=(- 1))
        v3 = (v3 + v4.to(v3.dtype))
        v4 = (v3 == (- 1)).to(v3.dtype)
        v3 = v3.permute(0, 2, 1)
        v3 = torch.nn.functional.linear(v3, self.linear.weight, self.linear.bias)
        v4 = torch.nn.functional.linear(v4, self.linear.weight, self.linear.bias)
        return (torch.max(v3, dim=(- 1))[0], torch.max(v4, dim=(- 1))[0])




func = Model().to('cuda')



x1 = torch.randn(1, 2, 2)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpz9vkguqm/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpz9vkguqm', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpz9vkguqm/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''