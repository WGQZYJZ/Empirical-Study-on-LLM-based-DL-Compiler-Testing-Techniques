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
        super(Model_v1, self).__init__()
        self.conv = torch.nn.ConvTranspose1d(2, 3, kernel_size=(2,), stride=(2,))
        self.linear = torch.nn.Linear(3, 3)

    def forward(self, x):
        x1 = self.conv(x)
        x2 = torch.relu(x1)
        x3 = self.linear(x1)
        return x3




func = Model().to('cuda')



x = torch.Tensor(1, 2, 13, 13)


test_inputs = [x]
