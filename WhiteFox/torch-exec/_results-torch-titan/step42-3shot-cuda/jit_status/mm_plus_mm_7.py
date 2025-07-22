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
        t1 = torch.mm(input1, input2)
        t2 = torch.mm(input3, input4)
        t = (t1 + t2)
        t3 = torch.sigmoid(t)
        t4 = torch.mm(input4, input5)
        t5 = torch.sigmoid(t4)
        t6 = torch.mm(input5, input3)
        t7 = torch.sigmoid(t6)
        t8 = torch.mm(input5, input2)
        t9 = torch.sigmoid(t8)
        output = torch.mm(input5, ((((t3 + t4) + t5) + t6) + t7))
        return (t9 + output)




func = Model().to('cuda')



input1 = torch.randn(3, 3)



input2 = torch.randn(3, 3)



input3 = torch.randn(3, 3)



input4 = torch.randn(3, 3)



input5 = torch.randn(3, 3)


test_inputs = [input1, input2, input3, input4, input5]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpz5p_fc7x/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpz5p_fc7x', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpz5p_fc7x/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''