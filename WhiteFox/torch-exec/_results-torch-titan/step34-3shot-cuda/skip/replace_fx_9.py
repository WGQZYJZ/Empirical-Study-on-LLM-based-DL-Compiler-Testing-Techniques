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
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 1, 1)
        self.dropout = nn.Dropout(0.1)

    def forward(self, x):
        return self.dropout(self.conv1(x))




func = model().to('cuda')

x = 1

test_inputs = [x]
