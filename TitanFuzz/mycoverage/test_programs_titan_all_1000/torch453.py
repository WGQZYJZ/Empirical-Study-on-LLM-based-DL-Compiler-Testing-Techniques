import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randint(0, 256, (1, 3, 10, 10), dtype=torch.uint8)
output_tensor = torch.Tensor.dequantize(input_tensor)