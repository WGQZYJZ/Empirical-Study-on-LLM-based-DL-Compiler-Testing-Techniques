'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LazyLinear\ntorch.nn.LazyLinear(out_features, bias=True, device=None, dtype=None)\n'
import torch
import torch.nn as nn
import torch
input = torch.randn(3, 5)
lazy_linear = nn.LazyLinear(5, 2)
output = lazy_linear(input)
print(output)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LazyLinear\ntorch.nn.LazyLinear(out_features, bias=True, device=None, dtype=None)\n'
import torch
import torch.nn as nn
import torch
input = torch.randn(3, 5)
lazy_linear = nn.LazyLinear(5, 2)