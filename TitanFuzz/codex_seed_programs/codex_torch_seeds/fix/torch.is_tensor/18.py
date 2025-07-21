'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.is_tensor\ntorch.is_tensor(obj)\n'
import torch
a = torch.tensor([1, 2, 3])
b = torch.tensor([1, 2, 3])
c = torch.tensor([1, 2, 3])
d = torch.tensor([1, 2, 3])
print('a: ', torch.is_tensor(a))
print('b: ', torch.is_tensor(b))
print('c: ', torch.is_tensor(c))
print('d: ', torch.is_tensor(d))