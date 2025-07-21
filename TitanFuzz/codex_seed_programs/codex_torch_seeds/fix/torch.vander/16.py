'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.vander\ntorch.vander(x, N=None, increasing=False)\n'
import torch
x = torch.arange(1, 5)
print('Input data: ', x)
print('torch.vander(x, N=None, increasing=False): ', torch.vander(x))
print('torch.vander(x, N=None, increasing=True): ', torch.vander(x, increasing=True))
print('torch.vander(x, N=3, increasing=False): ', torch.vander(x, N=3, increasing=False))