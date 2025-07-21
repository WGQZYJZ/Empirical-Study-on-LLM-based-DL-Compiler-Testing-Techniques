'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Softmin\ntorch.nn.Softmin(dim=None)\n'
import torch
import numpy as np
input_data = torch.randn(2, 3)
print(input_data)
output_data = torch.nn.Softmin(dim=0)
print(output_data)
output_data = torch.nn.Softmin(dim=1)
print(output_data)
output_data = torch.nn.Softmin(dim=None)
print(output_data)
output_data = torch.nn.Softmin(dim=(- 1))
print(output_data)
output_data = torch.nn.Softmin(dim=(- 2))
print(output_data)