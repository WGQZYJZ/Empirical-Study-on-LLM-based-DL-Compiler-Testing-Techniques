'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.layer_norm\ntorch.nn.functional.layer_norm(input, normalized_shape, weight=None, bias=None, eps=1e-05)\n'
import torch
import torch.nn.functional as F
input = torch.randn(20, 5, 10, 10)
output = F.layer_norm(input, [10, 10])
print(output)