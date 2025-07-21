'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.layer_norm\ntorch.nn.functional.layer_norm(input, normalized_shape, weight=None, bias=None, eps=1e-05)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
input_data = torch.randn(10, 10)
layer_norm_out = F.layer_norm(input_data, [10])
print(layer_norm_out)