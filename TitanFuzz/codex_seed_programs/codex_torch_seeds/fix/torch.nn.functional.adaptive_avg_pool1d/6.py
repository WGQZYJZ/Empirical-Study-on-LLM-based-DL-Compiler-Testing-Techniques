'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.adaptive_avg_pool1d\ntorch.nn.functional.adaptive_avg_pool1d(input, output_size)\n'
import torch
data = torch.randn(1, 1, 10)
print('Input data: ', data)
output = torch.nn.functional.adaptive_avg_pool1d(data, output_size=3)
print('Output data: ', output)
print('Output size: ', output.size())