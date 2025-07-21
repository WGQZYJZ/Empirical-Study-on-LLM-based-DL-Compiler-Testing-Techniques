'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.UpsamplingBilinear2d\ntorch.nn.UpsamplingBilinear2d(size=None, scale_factor=None)\n'
import torch
from torch.autograd import Variable
import torch
from torch.autograd import Variable
input_data = Variable(torch.randn(1, 1, 5, 5))
upsampling_bilinear2d = torch.nn.UpsamplingBilinear2d(size=None, scale_factor=2)
output_data = upsampling_bilinear2d(input_data)
print(output_data)