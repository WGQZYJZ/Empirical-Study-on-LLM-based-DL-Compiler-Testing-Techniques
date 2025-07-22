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

    def __init__(self):
        super().__init__()
        self.m = torch.nn.Linear(1, 1)



func = Model().to('cpu')


x = torch.randn(1, 1, 1)

test_inputs = [x]

# JIT_FAIL
'''
direct:
Module [Model] is missing the required "forward" function

jit:
Module [Model] is missing the required "forward" function
'''