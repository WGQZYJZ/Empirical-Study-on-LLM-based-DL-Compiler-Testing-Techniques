import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(1, 3, 224, 224, dtype=torch.float32)
output = torch.fake_quantize_per_tensor_affine(input_data, 1.0, 0, 0, 255)