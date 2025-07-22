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
        self.linear = Linear(4)

    def forward(self, x1):
        l1 = self.linear(x1)
        l2 = (l1 * torch.clamp(0, 6, (l1 + 3)))
        l3 = (l2 / 6)
        return l3



func = Model().to('cuda')



x1 = torch.randn((1, 4))


test_inputs = [x1]
