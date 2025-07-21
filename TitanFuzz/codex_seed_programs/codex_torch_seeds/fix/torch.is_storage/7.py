'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.is_storage\ntorch.is_storage(obj)\n'
import torch
tensor = torch.rand(2, 3)
print(tensor)
storage = torch.rand(2, 3)
print(storage)
print(torch.is_storage(tensor))
print(torch.is_storage(storage))