'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.embedding\ntorch.nn.functional.embedding(input, weight, padding_idx=None, max_norm=None, norm_type=2.0, scale_grad_by_freq=False, sparse=False)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import numpy as np
input = torch.LongTensor([[1, 2, 4, 5], [4, 3, 2, 9]])
weight = torch.randn(10, 3)
output = F.embedding(input, weight)
print(output)
print(output.shape)
print(weight.shape)
print(input.shape)