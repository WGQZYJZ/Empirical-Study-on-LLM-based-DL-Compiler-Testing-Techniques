import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]])
resize_result = torch.Tensor.resize_(input_tensor, (2, 2))
resize_result = torch.Tensor.resize_(input_tensor, (2, 2), memory_format=torch.channels_last)
resize_result = torch.Tensor.resize_(input_tensor, (2, 2), memory_format=torch.contiguous_format)