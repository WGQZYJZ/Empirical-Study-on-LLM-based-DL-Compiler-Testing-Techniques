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

    def forward(self, input1, input2, input3, input4):
        mm = torch.matmul(input1, input2).numpy()
        mm2 = torch.mm(input1, input2).numpy()
        mm3 = torch.mm(input3, input4).numpy()
        mm4 = torch.matmul(input3, input4).numpy()
        mm5 = np.dot(mm3, mm)
        mm6 = np.dot(input2.mm(input4), mm)
        return ((mm + mm2) + mm3)




func = Model().to('cuda')



input1 = torch.randn(5, 5)



input2 = torch.randn(5, 5)



input3 = torch.randn(5, 5)



input4 = torch.randn(5, 5)


test_inputs = [input1, input2, input3, input4]

# JIT_FAIL
'''
direct:
can't convert cuda:0 device type tensor to numpy. Use Tensor.cpu() to copy the tensor to host memory first.

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpsy_47joc/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpsy_47joc', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpsy_47joc/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''