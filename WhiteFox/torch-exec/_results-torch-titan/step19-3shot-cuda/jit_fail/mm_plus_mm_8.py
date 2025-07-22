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

    def __init__(self, in_size, h1_size, h2_size, num_classes):
        super(Model, self).__init__()
        self.classifier = nn.Sequential(nn.Linear(in_size, h1_size), nn.ReLU(), nn.Linear(h1_size, h2_size), nn.ReLU(), nn.Linear(h2_size, num_classes))

    def forward(self, input):
        return self.classifier(input)



in_size = 1
h1_size = 1
h2_size = 1
num_classes = 1

func = Model(in_size, h1_size, h2_size, num_classes).to('cuda')



x1 = torch.randn(2, 2)



x2 = torch.randn(4, 2)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 3 were given

jit:
forward() takes 2 positional arguments but 3 were given
'''