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

class MyModel(torch.nn.Module):

    def __init__(self):
        super(MyModel, self).__init__()
        self.fc1 = torch.nn.Linear(8, 2)

    def forward(self, x):
        x = self.fc1(x)
        x = torch.nn.functional.dropout(x)
        x = torch.rand_like(x)
        x = torch.nn.functional.dropout(x)
        x = torch.nn.functional.dropout(x)
        x = torch.nn.functional.dropout(x)
        x = torch.nn.functional.dropout(x)
        x = torch.nn.functional.dropout(x)
        x = torch.nn.functional.dropout(x)
        return x[0]



func = MyModel().to('cpu')

x = 1

test_inputs = [x]

# JIT_FAIL
'''
direct:
linear(): argument 'input' (position 1) must be Tensor, not int

jit:
linear(): argument 'input' (position 1) must be Tensor, not int
'''