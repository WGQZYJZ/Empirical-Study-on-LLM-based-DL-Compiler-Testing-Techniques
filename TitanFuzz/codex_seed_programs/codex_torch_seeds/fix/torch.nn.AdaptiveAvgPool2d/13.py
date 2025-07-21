'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveAvgPool2d\ntorch.nn.AdaptiveAvgPool2d(output_size)\n'
import torch
input = torch.randn(1, 1, 4, 4)
adaptive_avg_pool2d = torch.nn.AdaptiveAvgPool2d(output_size=2)
adaptive_avg_pool2d(input)