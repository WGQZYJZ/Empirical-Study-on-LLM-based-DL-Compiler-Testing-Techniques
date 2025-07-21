'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.digamma\ntorch.Tensor.digamma(_input_tensor)\n'
import torch
input_data = torch.randn(2, 3)
output_data = torch.Tensor.digamma(input_data)
print('Input tensor:\n', input_data)
print('Output tensor:\n', output_data)