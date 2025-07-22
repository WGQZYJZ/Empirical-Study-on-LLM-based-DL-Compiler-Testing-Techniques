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

    def forward(self, x1, x2):
        v1 = torch.nn.functional.linear(x2, self.linear.weight, self.linear.bias)
        v2 = v1.permute(0, 2, 1)
        lstm1 = torch.nn.LSTMCell(2, 2)
        v4 = lstm1(v2)
        lstm2 = torch.nn.LSTMCell(2, 2)
        v5 = lstm2(v4)
        return ((v1 + v4) + v5)




func = Model().to('cuda')



x1 = torch.randn(3, 2, 2)



x2 = torch.randn(3, 2, 2)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
LSTMCell: Expected input to be 1D or 2D, got 3D instead

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp5oc5wl5s/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp5oc5wl5s', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp5oc5wl5s/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''