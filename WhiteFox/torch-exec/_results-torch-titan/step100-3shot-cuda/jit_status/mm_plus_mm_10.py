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

    def forward(self, input):
        t11 = torch.mm(input, input)
        t12 = torch.mm(input, input)
        t13 = torch.mm(input, input)
        t14 = torch.mm(input, input)
        t21 = torch.mm(input, input)
        t22 = torch.mm(input, input)
        t23 = torch.mm(input, input)
        t31 = torch.mm(input, input)
        t32 = torch.mm(input, input)
        t33 = torch.mm(input, input)
        t34 = torch.mm(input, input)
        t35 = torch.mm(input, input)
        t41 = torch.mm(input, input)
        t42 = torch.mm(input, input)
        t43 = torch.mm(input, input)
        t44 = torch.mm(input, input)
        t45 = torch.mm(input, input)
        t51 = torch.mm(input, input)
        t52 = torch.mm(input, input)
        t53 = torch.mm(input, input)
        out1 = ((((((t11 + t12) + t13) + t14) + t21) + t22) + t23)
        out2 = ((((t31 + t32) + t33) + t34) + t35)
        out3 = ((((t41 + t42) + t43) + t44) + t45)
        out4 = ((t51 + t52) + t53)
        return (((out1 + out2) + out3) + out4)




func = Model().to('cuda')



input = torch.randn(100, 100)


test_inputs = [input]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmprada137y/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmprada137y', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmprada137y/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''