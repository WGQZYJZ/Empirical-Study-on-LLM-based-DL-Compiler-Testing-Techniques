import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(3, 5)
k = 3
dim = 1
largest = True
sorted = True
output_tensor = torch.Tensor.topk(input_tensor, k, dim, largest, sorted)