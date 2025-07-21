'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveAvgPool2d\ntorch.nn.AdaptiveAvgPool2d(output_size)\n'
import torch
input = torch.randn(1, 1, 4, 4)
avgpool = torch.nn.AdaptiveAvgPool2d((1, 1))
output = avgpool(input)
print(output)