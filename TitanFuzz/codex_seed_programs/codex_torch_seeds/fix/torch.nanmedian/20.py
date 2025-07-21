'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nanmedian\ntorch.nanmedian(input, dim=-1, keepdim=False, *, out=None)\n'
import torch
input_data = torch.tensor([[1, 2, 3, 4, 5], [5, 4, 3, 2, 1]])
result = torch.nanmedian(input_data)
print('result = ', result)
result = torch.nanmedian(input_data, dim=0)
print('result = ', result)
result = torch.nanmedian(input_data, dim=1)
print('result = ', result)