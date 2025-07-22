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



class Model(nn.Module):

    def forward(self, input1, input2, input3):
        t1 = nn.Tanh()(input1)
        t2 = (input1 + input3)
        t3 = nn.PReLU()((- t1))
        t4 = nn.Sigmoid()(input1)
        t5 = nn.Tanh()(input2)
        t6 = nn.Tanh()(input3)
        t7 = (input3 + input2)
        t8 = nn.ReLU()(input2)
        t9 = nn.ReLU()(t3)
        return ((((t5 + t6) + t7) + t8) + t9)




func = Model().to('cuda')



input1 = torch.randn(8, 8)



input2 = torch.randn(8, 8)



input3 = torch.randn(8, 8)


test_inputs = [input1, input2, input3]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu! (when checking argument for argument weight in method wrapper_CUDA___prelu_kernel)

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpnd43ro4m/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpnd43ro4m', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpnd43ro4m/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''