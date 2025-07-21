'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.QInt32Storage\ntorch.QInt32Storage(*args, **kwargs)\n'
import torch
data = [1, 2, 3, 4, 5]
out = torch.QInt32Storage(data)
print('torch.QInt32Storage(data): ', out)