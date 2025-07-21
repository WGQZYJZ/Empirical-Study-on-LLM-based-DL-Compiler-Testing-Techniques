import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.rand(2, 3, 4, 5, dtype=torch.float32)
_output_tensor = torch.Tensor.bfloat16(_input_tensor)