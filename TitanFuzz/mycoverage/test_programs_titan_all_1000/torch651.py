import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randint(0, 256, (1, 2, 3, 4), dtype=torch.uint8)
output = torch.dequantize(input_tensor)