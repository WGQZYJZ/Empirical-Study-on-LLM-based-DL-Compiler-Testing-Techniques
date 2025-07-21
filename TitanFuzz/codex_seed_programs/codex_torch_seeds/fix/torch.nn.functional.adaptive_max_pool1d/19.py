'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.adaptive_max_pool1d\ntorch.nn.functional.adaptive_max_pool1d(input, output_size, return_indices=False)\n'
import torch
from torch.autograd import Variable
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms
input = Variable(torch.randn(1, 4, 5))
print(input)
output = F.adaptive_max_pool1d(input, 3)
print(output)
(output, indices) = F.adaptive_max_pool1d(input, 3, return_indices=True)
print(output)
print(indices)