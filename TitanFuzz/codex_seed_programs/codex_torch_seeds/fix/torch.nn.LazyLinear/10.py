'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LazyLinear\ntorch.nn.LazyLinear(out_features, bias=True, device=None, dtype=None)\n'
import torch
input_data = torch.randn(3, 2)
linear = torch.nn.LazyLinear(2, bias=True, device=None, dtype=None)
print(linear(input_data))