import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
torch.Tensor.dequantize(input_tensor)
torch.Tensor.dequantize(input_tensor, scale=1.0, zero_point=0)