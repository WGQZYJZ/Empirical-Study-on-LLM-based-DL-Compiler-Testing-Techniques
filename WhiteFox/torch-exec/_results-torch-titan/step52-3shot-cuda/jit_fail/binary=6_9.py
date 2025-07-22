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
        self.fc = torch.nn.Linear(16, 16)

    def foward(self, x1):
        v1 = self.fc(x1)
        v2 = (v1 - other)
        return v2



func = Model().to('cuda')



x1 = torch.randn(1, 16)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Module [Model] is missing the required "forward" function

jit:
Module [Model] is missing the required "forward" function
'''