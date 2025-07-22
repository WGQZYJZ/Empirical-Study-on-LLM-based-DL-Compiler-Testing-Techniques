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

    def __init__(self, input_dim, num_heads, head_dim, dropout_p=0.0):
        super().__init__()
        self.input_dim = input_dim



input_dim = 1
num_heads = 1
head_dim = 1

func = Model(input_dim, num_heads, head_dim).to('cuda')

input_tensor = torch.randn(1, 1, 1)

test_inputs = [input_tensor]

# JIT_FAIL
'''
direct:
Module [Model] is missing the required "forward" function

jit:
Module [Model] is missing the required "forward" function
'''