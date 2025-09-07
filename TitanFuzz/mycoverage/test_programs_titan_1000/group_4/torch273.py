import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(10, 10)
cpu_tensor = torch.Tensor.cpu(input_tensor)
input_tensor = torch.randn(10, 10)
cpu_tensor = torch.Tensor.to(input_tensor, device='cpu')
input_tensor = torch.randn(10, 10)