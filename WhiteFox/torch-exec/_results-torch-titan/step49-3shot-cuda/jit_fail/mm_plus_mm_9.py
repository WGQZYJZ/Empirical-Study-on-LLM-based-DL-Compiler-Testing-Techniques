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

    def __init__(self, input_size=128, kernel_size=8, stride=1, padding=3, dilation=1, output_padding=0, groups=1, bias=True):
        super(Model, self).__init__()
        self.conv1 = torch.nn.Conv1d(3, 64, kernel_size, stride=stride, padding=padding, dilation=dilation, groups=groups, bias=bias, padding_mode='zeros')
        self.conv2 = torch.nn.Conv3d(64, input_size, kernel_size, stride=stride, padding=padding, dilation=dilation, groups=groups, bias=bias, padding_mode='zeros')

    def forward(self, x):
        conv1 = self.conv1(x)
        bn = F.batch_norm(conv1, None, None, None, None)
        relu = F.linear(bn, None, None, None, None)
        conv2 = self.conv2(relu)
        return conv2.flatten(1)




class Model(torch.nn.Module):

    def forward(self, inp):
        t1 = torch.mm(inp, inp)
        t2 = torch.mm(inp, inp)
        t3 = torch.mm(inp, t1)
        t4 = (t2 + t3)
        return (t4 + t1)




func = Model().to('cuda')



tensor1 = torch.randn(256, 100)


test_inputs = [tensor1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (256x100 and 256x100)

jit:
Failed running call_function <built-in method mm of type object at 0x7c560ba699e0>(*(FakeTensor(..., device='cuda:0', size=(256, 100)), FakeTensor(..., device='cuda:0', size=(256, 100))), **{}):
a and b must have same reduction dim, but got [256, 100] X [256, 100].

from user code:
   File "<string>", line 35, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''