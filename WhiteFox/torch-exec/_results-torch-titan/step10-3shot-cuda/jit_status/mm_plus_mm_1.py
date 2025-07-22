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

    def forward(self, input1, input2, input3, input4, input5):
        t1 = torch.matmul(input1, input2)
        t2 = torch.matmul(input3, input4)
        t3 = (t1 + t2)
        t4 = (t3 + input5)
        return t4




func = Model().to('cuda')



input1 = torch.randn(20, 20)



input2 = torch.randn(20, 20)



input3 = torch.randn(20, 20)



input4 = torch.randn(20, 20)



input5 = torch.randn(20, 20)


test_inputs = [input1, input2, input3, input4, input5]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpfat_9zws/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpfat_9zws', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpfat_9zws/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''