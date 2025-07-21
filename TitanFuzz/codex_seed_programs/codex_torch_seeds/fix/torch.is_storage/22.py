'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.is_storage\ntorch.is_storage(obj)\n'
import torch
a = torch.tensor([1, 2, 3])
b = torch.tensor([1, 2, 3])
print(torch.is_storage(a))
print(torch.is_storage(b))