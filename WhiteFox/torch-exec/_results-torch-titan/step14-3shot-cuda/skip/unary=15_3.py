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
        blocks = [torchvision.models.densenet121().features[:16], torchvision.models.densenet121().features[16:(16 + 24)], torchvision.models.densenet121().features[(16 + 24):((16 + 24) + 24)]]
        self.features = torch.nn.ModuleList(sum(blocks, []))

    def forward(self, x1):
        v0 = x1
        (v1, v1a) = self.features[0](v0)
        (v2, v2a) = self.features[1](v1a)
        (v3, v3a) = self.features[2](v2a)
        v4 = torch.cat([torch.unsqueeze(v1, 0), torch.unsqueeze(v2, 0), torch.unsqueeze(v3, 0), torch.unsqueeze(v3a, 0)], 0)
        return v4




func = Model().to('cuda')



x1 = torch.randn(1, 3, 256, 256)


test_inputs = [x1]
