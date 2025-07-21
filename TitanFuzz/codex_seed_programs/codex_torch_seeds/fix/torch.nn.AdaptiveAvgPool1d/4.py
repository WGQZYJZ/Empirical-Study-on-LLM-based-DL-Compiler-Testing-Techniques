'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveAvgPool1d\ntorch.nn.AdaptiveAvgPool1d(output_size)\n'
import torch
input_data = torch.randn(1, 1, 5)
print('input data: ', input_data)
adaptive_avg_pool1d = torch.nn.AdaptiveAvgPool1d(output_size=1)
output_data = adaptive_avg_pool1d(input_data)
print('output data: ', output_data)