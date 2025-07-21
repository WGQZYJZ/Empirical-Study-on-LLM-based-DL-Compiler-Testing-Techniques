'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.IntStorage\ntorch.IntStorage(*args, **kwargs)\n'
import torch
data = [1, 2, 3, 4]
storage = torch.IntStorage(data)
print(storage)