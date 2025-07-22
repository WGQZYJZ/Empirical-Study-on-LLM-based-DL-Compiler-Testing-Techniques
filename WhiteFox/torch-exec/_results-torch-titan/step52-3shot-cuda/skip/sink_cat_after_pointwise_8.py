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
        self.layer7 = torch.nn.Sequential((torch.nn.ReLU(), torch.nn.ReLU()))
        self.layer8 = torch.nn.Sequential((torch.nn.Tanh(), torch.nn.Tanh()))

    def forward(self, x):
        y = self.layer7(x)
        y = self.layer8(y)
        y1 = y.view(x.shape[0], (- 1))
        y2 = x.view(y.shape[0], (- 1))
        return torch.cat((y1, y2), dim=1)




func = Model().to('cuda')



x = torch.randn(2, 2, 2)


test_inputs = [x]
