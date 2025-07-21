'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LazyLinear\ntorch.nn.LazyLinear(out_features, bias=True, device=None, dtype=None)\n'
import torch
input_data = torch.rand(10, 3)
lazy_linear = torch.nn.LazyLinear(3, 2)
output_data = lazy_linear(input_data)
print('input_data: ', input_data)
print('output_data: ', output_data)