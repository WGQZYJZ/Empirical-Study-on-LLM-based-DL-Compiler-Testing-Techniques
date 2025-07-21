'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.all\ntorch.all(input, dim, keepdim=False, *, out=None)\n'
import torch
input_data = torch.tensor([[True, False], [False, True]])
result = torch.all(input_data)
print('result: ', result)
result = torch.all(input_data, dim=0)
print('result: ', result)
result = torch.all(input_data, dim=1)
print('result: ', result)
result = torch.all(input_data, dim=1, keepdim=True)
print('result: ', result)