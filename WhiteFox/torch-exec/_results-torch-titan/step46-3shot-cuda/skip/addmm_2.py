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
        super().__init__(self)

    def forward(self, x1, x2, x3, inp):
        v1 = torch.mm(x1, x2)
        v2 = (torch.mm(x3, x2) + v1)
        return v2




func = Model().to('cuda')



x1 = torch.randn(3, 3)



x2 = torch.randn(3, 3, requires_grad=True)



x3 = torch.randn(3, 3)



inp = torch.randn(3, 3, requires_grad=True)


test_inputs = [x1, x2, x3, inp]
