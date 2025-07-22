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
        t1 = torch.mm(input2, input3)
        if torch.eq(t1, t2):
            t2 = t1
        else:
            t2 = (t1 + t2)
        t3 = torch.mm(input1, input4)
        t3 = (t3 + t1)
        if torch.ne(t1, t3):
            t3 = (t3 + t2)
        else:
            t3 += t2
        if torch.lt(t1, t3):
            t1 = torch.mm(input1, input2)
        else:
            t1 = torch.mm(input1, input4)
        if torch.gt(t1, t3):
            t1 = torch.mm(input1, input4)
        else:
            t1 = torch.mm(input1, input2)
        if torch.le(t1, t2):
            t2 = torch.mm(input2, input3)
        else:
            t2 = torch.mm(input2, input4)
        if torch.ge(t1, t2):
            t2 = torch.mm(input2, input4)
        else:
            t2 = torch.mm(input2, input3)
        if torch.eq(t3, t1):
            t3 = torch.mm(input1, input2)
        else:
            t3 = torch.mm(input1, input4)
        if torch.ne(t3, t2):
            t3 = t2
        else:
            t3 = torch.mm(input1, input2)
        if torch.lt(t3, t1):
            t1 = torch.mm(input1, input4)
        else:
            t1 = torch.mm(input1, input3)
        if torch.gt(t3, t1):
            t1 = torch.mm(input1, input3)
        else:
            t1 = torch.mm(input1, input4)
        if torch.le(t1, t3):
            t3 = torch.mm(input1, input3)
        else:
            t3 = torch.mm(input1, input4)
        if torch.eq(t1, t3):
            t1 = torch.mm(input1, input2)
        else:
            t1 = torch.mm(input1, input3)
        if torch.eq(t1, input3):
            t1 = torch.mm(input1, input2)
        else:
            t1 = torch.mm(input1, input4)
        if torch.eq(t1, input2):
            t1 = torch.mm(input1, input3)
        else:
            t1 = torch.mm(input1, input4)
        t2 = (t1 + t3)
        return t2




func = Model().to('cuda')



input1 = torch.randn(8, 8)



input2 = torch.randn(8, 8)



input3 = torch.randn(8, 8)



input4 = torch.randn(8, 8)


test_inputs = [input1, input2, input3, input4]

# JIT_FAIL
'''
direct:
local variable 't2' referenced before assignment

jit:
local variable 't2' referenced before assignment
'''