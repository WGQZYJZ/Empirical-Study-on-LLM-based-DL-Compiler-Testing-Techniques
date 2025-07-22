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
        batch_size = input1.shape[0]
        t1 = torch.mm(input1, input2)
        t2 = torch.zeros([batch_size, batch_size], dtype=torch.float)
        for x in range(batch_size):
            for y in range(batch_size):
                t2[x][y] = (x + y)
        t2 = torch.mm(t2, input3)
        t3 = torch.mm(input4, t2)
        return (t1 - t3)




func = Model().to('cuda')



N = 10


N = 10


input1 = torch.randn(N, N)



N = 10


N = 10


input2 = torch.randn(N, N)



N = 10


N = 10


input3 = torch.randn(N, N)



N = 10


N = 10


input4 = torch.randn(N, N)


test_inputs = [input1, input2, input3, input4]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cpu and cuda:0! (when checking argument for argument mat2 in method wrapper_CUDA_mm)

jit:
Failed running call_function <built-in method mm of type object at 0x7faf32c699e0>(*(FakeTensor(..., size=(10, 10)), FakeTensor(..., device='cuda:0', size=(10, 10))), **{}):
Unhandled FakeTensor Device Propagation for aten.mm.default, found two different devices cpu, cuda:0

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''