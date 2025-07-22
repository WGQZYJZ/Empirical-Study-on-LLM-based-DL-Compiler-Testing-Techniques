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



class SubsequentMask(torch.nn.Module):

    def forward(self, x):
        N = x.shape[1]
        mask = torch.tril(torch.ones(N, N))
        return mask.unsqueeze(0)




class Model(torch.nn.Module):

    def __init__(self, num_layers, num_heads):
        self.num_layers = num_layers
        self.num_heads = num_heads
        self.d_k = (512 // num_heads)
        self.layers = torch.nn.ModuleList([EncoderLayer(self.d_k, self.num_heads) for _ in range(self.num_layers)])
        self.fc = torch.nn.Linear(((self.d_k * self.num_heads) * 2), d_model)
        self.subsequent_mask = SubsequentMask()

    def forward(self, x):
        key_masks = [self.subsequent_mask(x) for _ in range(self.num_layers)]
        value_mask = self.subsequent_mask(x)
        context_list = []
        for i in range(self.num_layers):
            x = self.layers[i](x, key_masks[i], value_mask)
            context_list.append(x)
        output = torch.cat(context_list, dim=1)
        output = self.fc(x)
        return output



num_layers = 1
num_heads = 1

func = Model(num_layers, num_heads).to('cuda')



x = torch.randn(1, 49, 60, 512)


test_inputs = [x]
