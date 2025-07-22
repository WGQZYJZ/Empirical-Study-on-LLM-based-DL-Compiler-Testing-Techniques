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



class Model(torch.nn.Layer):

    def __init__(self):
        super(Model, self).__init__()
        self.linear = torch.nn.Linear(19, 19)

    def forward(self, x):
        v1 = self.linear(x)
        v2 = (v1 - other)
        return v2



func = Model().to('cuda')



x = torch.randn(20, 19)


test_inputs = [x]
