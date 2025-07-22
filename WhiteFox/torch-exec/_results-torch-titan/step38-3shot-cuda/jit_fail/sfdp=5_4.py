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
        self.heads = 1024
        self.seq_len = 128
        self.dim = 64

    def forward(self, input1, input2, input3, input4):
        concat3 = torch.cat((input1, input4), 1)
        batch1 = torch.flatten(concat3, 1)
        matmul1 = torch.matmul(batch1, input3)
        output1 = torch.reshape(matmul1, (1, 128, 1024, 1))
        return output1




func = Model().to('cuda')



input1 = torch.randn(1, 256, 1, 1)



input2 = torch.randn(1, 256, 1, 1)



input3 = torch.randn(256, 1)



input4 = torch.randn(1, 256, 1, 1)


test_inputs = [input1, input2, input3, input4]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x512 and 256x1)

jit:
Failed running call_function <built-in method matmul of type object at 0x769abc0699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 512)), FakeTensor(..., device='cuda:0', size=(256, 1))), **{}):
a and b must have same reduction dim, but got [1, 512] X [256, 1].

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''