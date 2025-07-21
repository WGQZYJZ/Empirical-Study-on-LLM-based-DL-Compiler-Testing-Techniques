'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveAvgPool1d\ntorch.nn.AdaptiveAvgPool1d(output_size)\n'
import torch
input = torch.randn(1, 1, 5)
print(input)
avgpool = torch.nn.AdaptiveAvgPool1d(1)
output = avgpool(input)
print(output)
print(output.shape)