import torch
from torch import nn
from torch.autograd import Variable
tensors = []
for i in range(5):
    tensors.append(torch.randn(10, 10))
result = torch.linalg.multi_dot(tensors)