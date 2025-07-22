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
        self.w1 = torch.randn(1, 1)
        self.w2 = torch.randn(1, 1)
        self.w3 = torch.randn(1, 1)




class Model(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.w1 = torch.randn(4, 4)
        self.w2 = torch.randn(4, 4)
        self.w3 = torch.randn(4, 4)
        self.w4 = torch.randn(4, 4)
        self.w5 = torch.randn(4, 4)
        self.w6 = torch.randn(4, 4)




func = Model().to('cuda')

input_tensor = torch.randn(1, 1, 1)

test_inputs = [input_tensor]

# JIT_FAIL
'''
direct:
Module [Model] is missing the required "forward" function

jit:
Module [Model] is missing the required "forward" function
'''