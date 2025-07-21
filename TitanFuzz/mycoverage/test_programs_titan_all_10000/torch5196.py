import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.arange(start=1, end=17, dtype=torch.float32).reshape(2, 2, 4)
output_tensor = torch.Tensor.dsplit(input_tensor, split_size_or_sections=2)
output_tensor = torch.Tensor.dsplit(input_tensor, split_size_or_sections=[2, 1])
output_tensor = torch.Tensor.dsplit(input_tensor, split_size_or_sections=[2, 2, 2])