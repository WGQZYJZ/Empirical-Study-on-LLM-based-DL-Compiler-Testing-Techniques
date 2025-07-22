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

    def forward(self, input1, input2, input3, input4, input5, input6):
        t1 = torch.mm(input1, input3)
        t2 = torch.mm(input2, input4)
        t3 = torch.mm(input5, input6)
        t4 = torch.mm(input1, input3)
        t5 = torch.mm(input2, input4)
        t6 = torch.mm(input5, input6)
        t7 = torch.mm(input1, input6)
        t8 = torch.mm(input2, input5)
        t9 = torch.mm(input3, input6)
        t10 = torch.mm(input1, input3)
        t11 = torch.mm(input2, input4)
        t12 = torch.mm(input5, input6)
        t13 = torch.mm(input3, input5)
        t14 = torch.mm(input1, input2)
        t15 = torch.mm(input4, input6)
        t16 = ((t1 + t2) + t3)
        t17 = ((t4 + t5) + t6)
        t18 = ((t7 + t8) + t9)
        t19 = ((t10 + t11) + t12)
        t20 = ((t13 + t14) + t15)
        t21 = (t16 + t17)
        t22 = (t18 + t19)
        t23 = torch.mm(t21, t22)
        return t23




func = Model().to('cuda')



input1 = torch.randn(3, 3)



input2 = torch.randn(3, 3)



input3 = torch.randn(3, 3)



input4 = torch.randn(3, 3)



input5 = torch.randn(3, 3)



input6 = torch.randn(3, 3)


test_inputs = [input1, input2, input3, input4, input5, input6]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpfz3yiia0/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpfz3yiia0', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpfz3yiia0/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''