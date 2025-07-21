'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.amin\ntorch.amin(input, dim, keepdim=False, *, out=None)\n'
import torch
import torch
input_tensor = torch.rand(3, 3)
print('input_tensor: ', input_tensor)
result = torch.amin(input_tensor, 1, keepdim=True)
print('torch.amin(input_tensor, 1, keepdim=True): ', result)
result = torch.amin(input_tensor, 1, keepdim=False)
print('torch.amin(input_tensor, 1, keepdim=False): ', result)