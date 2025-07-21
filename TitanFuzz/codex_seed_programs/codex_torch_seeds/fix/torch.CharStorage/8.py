'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.CharStorage\ntorch.CharStorage(*args, **kwargs)\n'
import torch
print(torch.__version__)
data = [1, 2, 3, 4, 5]
storage = torch.CharStorage(data)
print(storage)