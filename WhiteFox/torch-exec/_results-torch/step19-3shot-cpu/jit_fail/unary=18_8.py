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

class MyModule(torch.nn.Module):

    def __init__(self):
        super().__init__()

    def forwadi(self, x):
        x_new = x.view(-1, 8, 2, int(x.size(2) / 2), int(x.size(3) / 2))
        x_new = x_new.view(-1, 8, 1, int(x.size(2) / 2), int(x.size(3) / 2))
        return x_new



func = MyModule().to('cpu')

input_tensor = torch.randn(1, 1, 1)

test_inputs = [input_tensor]

# JIT_FAIL
'''
direct:
Module [MyModule] is missing the required "forward" function

jit:
Module [MyModule] is missing the required "forward" function
'''