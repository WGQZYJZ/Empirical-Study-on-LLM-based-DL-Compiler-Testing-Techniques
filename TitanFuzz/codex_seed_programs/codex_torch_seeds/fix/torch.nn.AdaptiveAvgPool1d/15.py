'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveAvgPool1d\ntorch.nn.AdaptiveAvgPool1d(output_size)\n'
import torch
data = torch.randn(1, 1, 4)
pool = torch.nn.AdaptiveAvgPool1d(output_size=2)
print(pool(data))
pool = torch.nn.AdaptiveAvgPool1d(output_size=1)
print(pool(data))
pool = torch.nn.AdaptiveAvgPool1d(output_size=3)
print(pool(data))