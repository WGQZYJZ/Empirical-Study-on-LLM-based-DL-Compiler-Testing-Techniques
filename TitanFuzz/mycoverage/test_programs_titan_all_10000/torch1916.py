import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
divisor = torch.tensor([1, 2, 3])
output_tensor = torch.Tensor.remainder_(input_tensor, divisor)