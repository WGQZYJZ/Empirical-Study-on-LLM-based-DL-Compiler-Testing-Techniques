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

    def forward(self, inputs):
        t1 = torch.mm(inputs[:, 3::2], inputs[:, 1::2])
        t2 = torch.mm(inputs[:, ::2], inputs[:, 2::2])
        t3 = torch.mm(inputs[:, 2:7], inputs[:, 4:9])
        t4 = torch.mm(inputs[:, 1:5], inputs[:, 6:10])
        t5 = (t1 + t2)
        return ((t3 * t4) * t5)




func = Model().to('cuda')



input1 = torch.randn(3, 10)



input2 = torch.randn(5, 10)



input3 = torch.randn(2, 10)



input4 = torch.randn(4, 10)


test_inputs = [input1, input2, input3, input4]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 5 were given

jit:
forward() takes 2 positional arguments but 5 were given
'''