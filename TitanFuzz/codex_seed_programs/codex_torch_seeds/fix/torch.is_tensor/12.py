'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.is_tensor\ntorch.is_tensor(obj)\n'
import torch
a = torch.randn(2, 3)
b = torch.randn(2, 3)
print(torch.is_tensor(a))
print(torch.is_tensor(b))
print(torch.is_tensor((a + b)))
print(torch.is_storage(a))
print(torch.is_storage(b))
print(torch.is_storage((a + b)))