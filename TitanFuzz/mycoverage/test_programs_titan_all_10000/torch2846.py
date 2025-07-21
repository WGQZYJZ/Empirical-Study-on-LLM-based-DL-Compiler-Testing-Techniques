import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn((2, 3), dtype=torch.float32)
output_tensor = torch.Tensor.conj_physical_(input_tensor)