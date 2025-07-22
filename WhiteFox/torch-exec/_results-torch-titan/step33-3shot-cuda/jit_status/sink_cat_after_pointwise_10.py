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

    def forward(self, x):
        if (x.shape[1] == 2):
            y = torch.relu(x)
            z = torch.tanh(y)
        else:
            y1 = torch.tanh(x)
            y2 = torch.relu(x)
            z = torch.cat((y1, y2), dim=0)
            z = z.view(z.shape[0], (- 1)).softmax(dim=1)
        return z




func = Model().to('cuda')



x = torch.randn(2, 2, 2)


test_inputs = [x]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp9enppc8c/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp9enppc8c', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp9enppc8c/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''