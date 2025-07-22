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
        return mm + mm2 + mm3



func = Model().to('cpu')


input1 = torch.randn(5, 5)

input2 = torch.randn(5, 5)

input3 = torch.randn(5, 5)

input4 = torch.randn(5, 5)

test_inputs = [input1, input2, input3, input4]

# CRASH
'''
crash:
The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()
'''