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
        self.linear1 = LinearLayer(1024, 1024)

    def forward(self, l):
        l1 = self.linear1(l)
        l2 = (l1 + 3)
        l3 = torch.clamp_min(l2, 0)
        l4 = torch.clamp_max(l3, 6)
        l5 = (l4 / 6)
        return l5



func = Model().to('cuda')



l = torch.ones(1, 1024)


test_inputs = [l]
