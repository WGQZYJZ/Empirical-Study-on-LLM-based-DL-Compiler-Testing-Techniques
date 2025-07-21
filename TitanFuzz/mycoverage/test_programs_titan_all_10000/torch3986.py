import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(4, 4)
quantized_data = torch.fake_quantize_per_tensor_affine(input_data, scale=0.1, zero_point=5, quant_min=0, quant_max=10)
input_data = torch.rand(4, 2, 4)