import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(3, 3, dtype=torch.float32)
output_tensor = torch.Tensor.bfloat16(input_tensor, memory_format=torch.preserve_format)
output_tensor = torch.Tensor.bfloat16(input_tensor, memory_format=torch.preserve_format)