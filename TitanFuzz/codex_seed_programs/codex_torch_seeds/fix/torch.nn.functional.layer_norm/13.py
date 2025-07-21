'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.layer_norm\ntorch.nn.functional.layer_norm(input, normalized_shape, weight=None, bias=None, eps=1e-05)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch
import torch.nn as nn
import torch.nn.functional as F
x = torch.randn(2, 3, 4)
output = F.layer_norm(x, [3, 4])
print(output)