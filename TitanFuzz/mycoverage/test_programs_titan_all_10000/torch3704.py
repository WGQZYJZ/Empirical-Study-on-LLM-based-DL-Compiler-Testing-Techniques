import torch
from torch import nn
from torch.autograd import Variable
tensors = torch.randint(0, 256, (2, 2), dtype=torch.uint8)
tensors = tensors.float()
result = torch.dequantize(tensors)