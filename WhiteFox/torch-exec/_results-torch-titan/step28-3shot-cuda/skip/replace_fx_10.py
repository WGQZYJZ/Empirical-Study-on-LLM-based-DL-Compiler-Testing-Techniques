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



class model(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.layer = torch.nn.Linear(2, 2)
        self.dropout1 = torch.nn.Dropout(p=0.4)
        self.dropout2 = torch.nn.Dropout(p=0.2)
        self.relu = torch.nn.ReLU()

    def forward(self, x):
        a = self.layer(x)
        a = self.dropout1(a)
        a = self.relu(a)
        b = self.layer(a)
        b = self.relu(b)
        c = self.dropout1(b)
        c = self.layer(c)
        c = self.dropout2(c)
        c = self.relu(c)
    return c




func = model().to('cuda')



x1 = torch.randn(2, 2, 2, 2)


test_inputs = [x1]
