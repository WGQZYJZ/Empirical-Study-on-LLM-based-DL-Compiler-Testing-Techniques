'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isreal\ntorch.isreal(input)\n'
import torch
tensor = torch.randn(3, 3)
print('tensor: ', tensor)
print('torch.isreal(tensor): ', torch.isreal(tensor))