'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Bilinear\ntorch.nn.Bilinear(in1_features, in2_features, out_features, bias=True, device=None, dtype=None)\n'
import torch
from torch.nn import Bilinear
input1 = torch.randn(2, 3)
input2 = torch.randn(2, 5)
bilinear = Bilinear(3, 5, 1)
output = bilinear(input1, input2)
print('input1: ', input1)
print('input2: ', input2)
print('output: ', output)