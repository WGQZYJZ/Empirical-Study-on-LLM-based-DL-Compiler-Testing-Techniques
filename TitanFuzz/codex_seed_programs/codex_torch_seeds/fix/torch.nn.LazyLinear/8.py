'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LazyLinear\ntorch.nn.LazyLinear(out_features, bias=True, device=None, dtype=None)\n'
import torch
input_data = torch.randn(1, 3)
linear = torch.nn.LazyLinear(3, 2)
print(linear(input_data))