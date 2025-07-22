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
        self.conv1d = torch.nn.Conv1d(2, 2, 3)
        self.batch_norm = torch.nn.BatchNorm1d(2)

    def forward(self, x):
        x1 = self.conv1d(x)
        y1 = self.batch_norm(x1)
        x2 = self.conv1d(x)
        y2 = torch.nn.functional.batch_norm(x2, self.batch_norm.running_mean, self.batch_norm.running_var, self.batch_norm.weight, self.batch_norm.bias, False, 0.1)
        return (x1, x2)



func = Model().to('cuda')



x = torch.randn(1, 2, 8)


test_inputs = [x]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp0mk9cgqa/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp0mk9cgqa', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp0mk9cgqa/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''