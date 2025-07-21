import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(3, 3)
index = torch.tensor([0, 2])
tensor2 = torch.tensor([1.0, 1.0])
output_tensor = torch.Tensor.index_add(input_tensor, 0, index, tensor2)
input_tensor = torch.randn(3, 3)
index = torch.tensor([0, 2])
tensor2 = torch.t