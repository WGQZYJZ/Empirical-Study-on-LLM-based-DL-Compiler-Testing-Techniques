'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.unsqueeze\ntorch.unsqueeze(input, dim)\n'
import torch
data = torch.tensor([[1, 2], [3, 4]])
result = torch.unsqueeze(data, dim=0)
print('result: ', result)
result = torch.unsqueeze(data, dim=1)
print('result: ', result)
result = torch.unsqueeze(data, dim=(- 1))
print('result: ', result)