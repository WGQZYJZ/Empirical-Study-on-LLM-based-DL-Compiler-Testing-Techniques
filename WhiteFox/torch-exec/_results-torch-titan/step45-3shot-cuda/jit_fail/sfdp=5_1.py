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
        self.seq_len = 80
        self.dim = 40

    def forward(self, input):
        conv1 = nn.Conv1d(input.shape[1], 50, 32)
        conv1 = nn.ReLU(conv1(input))
        conv1 = nn.Conv1d(50, 50, 32, stride=2)
        conv1 = nn.ReLU(conv1(conv1))
        conv1 = nn.Conv1d(50, 50, 32)
        conv1 = nn.ReLU(conv1(conv1))
        conv1 = nn.Conv1d(input.shape[1], 50, 32)
        conv2 = nn.ReLU(conv1(input))
        conv2 = nn.Conv1d(50, 50, 32, stride=2)
        conv2 = nn.ReLU(conv2(conv2))
        conv2 = nn.Conv1d(50, 50, 32)
        conv2 = nn.ReLU(conv2(conv2))
        conv2 = nn.Conv1d(50, 50, 32)
        conv2 = nn.ReLU(conv2(conv2))
        conv2 = nn.Conv1d(input.shape[1], 50, 32)
        conv3 = nn.ReLU(conv2(input))
        conv3 = nn.Conv1d(50, 50, 32, stride=2)
        conv3 = nn.ReLU(conv3(conv3))
        conv3 = nn.Conv1d(50, 50, 32)
        conv3 = nn.ReLU(conv3(conv3))
        conv3 = nn.Conv1d(50, 50, 32)
        conv3 = nn.ReLU(conv3(conv3))
        conv3 = nn.Conv1d(50, 50, 32)
        concat = torch.cat((conv1, conv2, conv3))
        return concat




func = Model().to('cuda')



input = torch.randn(80, 1, 40)


test_inputs = [input]

# JIT_FAIL
'''
direct:
Input type (torch.cuda.FloatTensor) and weight type (torch.FloatTensor) should be the same

jit:
conv1d() received an invalid combination of arguments - got (Conv1d, Parameter, Parameter, tuple, tuple, tuple, int), but expected one of:
 * (Tensor input, Tensor weight, Tensor bias, tuple of ints stride, tuple of ints padding, tuple of ints dilation, int groups)
      didn't match because some of the arguments have invalid types: (!Conv1d!, !Parameter!, !Parameter!, !tuple of (int,)!, !tuple of (int,)!, !tuple of (int,)!, int)
 * (Tensor input, Tensor weight, Tensor bias, tuple of ints stride, str padding, tuple of ints dilation, int groups)
      didn't match because some of the arguments have invalid types: (!Conv1d!, !Parameter!, !Parameter!, !tuple of (int,)!, !tuple of (int,)!, !tuple of (int,)!, int)

'''