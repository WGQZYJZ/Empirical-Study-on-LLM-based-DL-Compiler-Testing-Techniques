import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 2, 3, 4)
scale = 0.5
zero_point = 1
quant_min = 0
quant_max = 2
output = torch.fake_quantize_per_tensor_affine(input, scale, zero_point, quant_min, quant_max)
input = torch.randn(4, 2, 3, 4)
scales = torch.tensor([0.5, 0.5])
zero_points = torch.tensor([1, 1])