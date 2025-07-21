'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveAvgPool1d\ntorch.nn.AdaptiveAvgPool1d(output_size)\n'
import torch
input_data = torch.randn(1, 1, 10)
print(input_data)
adaptive_avg_pool_1d = torch.nn.AdaptiveAvgPool1d(5)
print(adaptive_avg_pool_1d(input_data))