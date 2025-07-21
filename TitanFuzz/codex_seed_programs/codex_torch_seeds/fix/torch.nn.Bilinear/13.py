'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Bilinear\ntorch.nn.Bilinear(in1_features, in2_features, out_features, bias=True, device=None, dtype=None)\n'
import torch
import torch.nn as nn
input_data_1 = torch.randn(8, 10)
input_data_2 = torch.randn(8, 20)
bilinear = nn.Bilinear(10, 20, 5)
output = bilinear(input_data_1, input_data_2)
print(output.size())