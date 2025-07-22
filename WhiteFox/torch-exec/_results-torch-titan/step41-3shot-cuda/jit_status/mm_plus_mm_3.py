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

    def forward(self, input1, input2, input3):
        t0 = torch.mm(input1, input2)
        t1 = torch.mm(input2, input1)
        t2 = torch.mm(input3, input2)
        t3 = torch.mm(input3, input1)
        t4 = (t2 + t1)
        t5 = (t0 + t3)
        t6 = torch.mm(input1, input3)
        return ((t6 + t5) + t4)




func = Model().to('cuda')



input1 = torch.randn(3, 3)



input2 = torch.randn(3, 3)



input3 = torch.randn(3, 3)


test_inputs = [input1, input2, input3]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpym239xkk/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpym239xkk', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpym239xkk/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''