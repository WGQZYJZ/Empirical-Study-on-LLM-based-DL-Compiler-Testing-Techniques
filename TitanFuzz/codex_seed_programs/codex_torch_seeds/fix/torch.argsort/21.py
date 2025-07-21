'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.argsort\ntorch.argsort(input, dim=-1, descending=False)\n'
import torch
input_data = torch.randn(3, 4)
print('input data:', input_data)
sorted_indices = torch.argsort(input_data, dim=(- 1), descending=True)
print('sorted indices:', sorted_indices)
sorted_data = torch.gather(input_data, dim=(- 1), index=sorted_indices)
print('sorted data:', sorted_data)