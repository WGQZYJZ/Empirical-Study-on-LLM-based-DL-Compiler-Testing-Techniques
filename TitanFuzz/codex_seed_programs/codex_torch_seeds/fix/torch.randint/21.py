'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.randint\ntorch.randint(low=0, high, size, *, generator=None, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
import torch
input_data = torch.randint(low=0, high=10, size=(4, 4))
print('Input data:', input_data)
result = torch.randint(low=0, high=10, size=(4, 4))
print('Result:', result)
print('dtype:', result.dtype)
print('device:', result.device)
print('layout:', result.layout)
print('requires_grad:', result.requires_grad)
print('shape:', result.shape)
print('size:', result.size())