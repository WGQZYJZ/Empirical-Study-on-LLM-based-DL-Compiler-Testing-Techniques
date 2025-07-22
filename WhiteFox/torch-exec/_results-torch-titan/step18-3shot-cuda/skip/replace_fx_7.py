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
        super(Model, self).__init__()
        self.drop1 = dropout.Dropout(0.4)
        self.conv1 = torch.nn.Conv1d(4, 8, 4, bias=False)
        self.conv2 = torch.nn.Conv1d(8, 4, 4, bias=False)

    def forward(self, data):
        x = self.conv1(data)
        x = self.drop1(x)
        x = self.conv2(x)
        out = torch.sum(x)
        return out




func = Model().to('cuda')



data1 = torch.randn(1, 4, 4)


test_inputs = [data1]
