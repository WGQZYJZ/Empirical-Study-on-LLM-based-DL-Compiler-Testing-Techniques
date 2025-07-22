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

class Model(torch.nn.Mo):

    def __init__(self):
        super().__init__()

    def forward(self, x):
        y = torch.cat((x, x, x, x), dim=1)
        y = y.view(y.shape[0], -1)
        z1 = torch.tanh(y)
        z2 = torch.relu(y)
        y = z1
        y = y.view_as(z2)
        return y



func = Model().to('cpu')


x = torch.randn(2, 3, 4)

test_inputs = [x]
