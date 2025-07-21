import torch
from torch import nn
from torch.autograd import Variable
dtype = torch.qint8
(N, C, H, W) = (2, 3, 4, 5)
input = torch.randn(N, C, H, W, dtype=torch.float)
scale = 1.0
zero_point = 0
quant_min = 0
quant_max = 255
output = torch.fake_quantize_per_tensor_affine(input, scale, zero_point, quant_min, quant_max)