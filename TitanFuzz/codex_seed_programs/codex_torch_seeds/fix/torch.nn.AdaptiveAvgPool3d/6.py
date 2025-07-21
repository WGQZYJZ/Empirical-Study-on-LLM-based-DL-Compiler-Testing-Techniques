'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveAvgPool3d\ntorch.nn.AdaptiveAvgPool3d(output_size)\n'
import torch
input_data = torch.randn(20, 16, 50, 32, 45)
output_size = (1, 1, 1)
avg_pool_3d = torch.nn.AdaptiveAvgPool3d(output_size)
output = avg_pool_3d(input_data)
print('input size: ', input_data.size())
print('output size: ', output.size())