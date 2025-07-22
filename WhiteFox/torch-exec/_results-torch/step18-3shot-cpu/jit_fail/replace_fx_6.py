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

    def forward(self, args, kwargs):
        t1 = torch.nn.functional.dropout(input_1=args, p=0.3)
        t2 = torch.nn.functional.dropout(input=kwargs, p=0.4)
        return t2 + t1



func = MyModel().to('cpu')


args1 = torch.zeros(3, 4)

kwargs1 = torch.ones(3, 4)

test_inputs = [args1, kwargs1]

# JIT_FAIL
'''
direct:
dropout() got an unexpected keyword argument 'input_1'

jit:
dropout() got an unexpected keyword argument 'input_1'
'''