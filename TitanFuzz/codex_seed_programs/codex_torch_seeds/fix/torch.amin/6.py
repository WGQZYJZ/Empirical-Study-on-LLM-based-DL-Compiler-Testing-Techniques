'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.amin\ntorch.amin(input, dim, keepdim=False, *, out=None)\n'
import torch
input_data = torch.randn(3, 4)
print('input_data:', input_data)
result = torch.amin(input_data, dim=0, keepdim=False)
print('result:', result)
result = torch.amin(input_data, dim=1, keepdim=False)
print('result:', result)
result = torch.amin(input_data, dim=1, keepdim=True)
print('result:', result)