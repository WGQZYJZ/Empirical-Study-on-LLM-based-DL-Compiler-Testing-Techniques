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

    def forward(self, X):
        yhat_p1 = self.linear(X).add(1).pow((- 2)).prod((- 1)).clamp(min=1e-15).repeat(2, 2).flatten().add(1.0).reciprocal().add(1e-15)
        yhat = torch.stack((yhat_p1, yhat_p1), dim=1)
        return yhat




func = Model().to('cuda')



X = torch.randn(1, 2, 2)


test_inputs = [X]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmprl8zhnwm/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmprl8zhnwm', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmprl8zhnwm/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''