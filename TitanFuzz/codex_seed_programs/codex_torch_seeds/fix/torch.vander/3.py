'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.vander\ntorch.vander(x, N=None, increasing=False)\n'
import torch
x = torch.arange(1, 5, dtype=torch.float)
print('x:', x)
print('torch.vander(x):', torch.vander(x))
print('torch.vander(x, increasing=True):', torch.vander(x, increasing=True))
print('torch.vander(x, N=2):', torch.vander(x, N=2))
print('torch.vander(x, N=3):', torch.vander(x, N=3))
print('torch.vander(x, N=4):', torch.vander(x, N=4))
print('torch.vander(x, N=5):', torch.vander(x, N=5))