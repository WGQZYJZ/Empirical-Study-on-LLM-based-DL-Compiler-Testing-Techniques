import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8]])
_output_tensor = torch.Tensor.float(_input_tensor, memory_format=torch.preserve_format)