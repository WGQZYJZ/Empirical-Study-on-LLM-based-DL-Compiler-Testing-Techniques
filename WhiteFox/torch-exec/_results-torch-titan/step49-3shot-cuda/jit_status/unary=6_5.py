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
        self.conv1 = torch.nn.Conv2d(3, 64, 3, stride=2, padding=1)
        self.conv2 = torch.nn.Conv2d(64, 64, 3, stride=2, padding=1)
        self.conv3 = torch.nn.Conv2d(64, 128, 3, stride=2, padding=1)

    def forward(self, x):
        t1 = self.conv1(x)
        t2 = self.conv2(t1)
        t3 = self.conv3(t2)
        t4 = torch.flatten(t3, 1)
        t5 = torch.flatten(t4, 1)
        t6 = torch.flatten(x, 1)
        t7 = torch.flatten(x, 2)
        t8 = torch.flatten(x, 3)
        t9 = torch.flatten(x, (- 1))
        t10 = torch.flatten(x, (- 2))
        t11 = torch.flatten(x, 0)
        return (t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11)




func = Model().to('cuda')



x = torch.randn(1, 3, 64, 64)


test_inputs = [x]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpsj5vmbce/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpsj5vmbce', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpsj5vmbce/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''