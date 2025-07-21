'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.layer_norm\ntorch.nn.functional.layer_norm(input, normalized_shape, weight=None, bias=None, eps=1e-05)\n'
import torch
input_data = torch.randn(3, 4, 5)
print('input_data: ', input_data)
output = torch.nn.functional.layer_norm(input_data, normalized_shape=(4, 5))
print('output: ', output)