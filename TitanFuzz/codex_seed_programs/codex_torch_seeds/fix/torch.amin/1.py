'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.amin\ntorch.amin(input, dim, keepdim=False, *, out=None)\n'
import torch
x = torch.randint(low=0, high=10, size=(3, 4))
print('Input data: ', x)
print('torch.amin(x, dim=1): ', torch.amin(x, dim=1))
print('torch.amin(x, dim=1, keepdim=True): ', torch.amin(x, dim=1, keepdim=True))
print('torch.amin(x, dim=1, keepdim=True): ', torch.amin(x, dim=1, keepdim=True).shape)
print('torch.amin(x, dim=1, keepdim=False): ', torch.amin(x, dim=1, keepdim=False))