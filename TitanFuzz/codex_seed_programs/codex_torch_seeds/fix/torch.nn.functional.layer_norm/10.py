'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.layer_norm\ntorch.nn.functional.layer_norm(input, normalized_shape, weight=None, bias=None, eps=1e-05)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch
input = torch.rand(3, 4, requires_grad=True)
output = F.layer_norm(input, normalized_shape=[4])
print(output)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.leaky_relu\ntorch.nn.functional.leaky_relu(input, negative_slope=0.01, inplace=False)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch
input = torch.rand(3, 4, requires_grad=True)
output = F.leaky_relu(input, negative_slope=0.01)
print(output)