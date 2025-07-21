'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Bilinear\ntorch.nn.Bilinear(in1_features, in2_features, out_features, bias=True, device=None, dtype=None)\n'
import torch
import torch
in1_features = 2
in2_features = 3
out_features = 4
bilinear = torch.nn.Bilinear(in1_features, in2_features, out_features)
print(bilinear)
input1 = torch.randn(1, in1_features)