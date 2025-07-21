import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(20, 6)
indices_or_sections = [3, 5, 6, 5]
output = torch.tensor_split(input, indices_or_sections, dim=0)
for tensor in output:
    print(f'tensor size: {tensor.size()}')
indices_or_sections = 4
output = torch.tensor_split(input, indices_or_sections, dim=0)
for tensor in output:
    print(f'tensor size: {tensor.size()}')