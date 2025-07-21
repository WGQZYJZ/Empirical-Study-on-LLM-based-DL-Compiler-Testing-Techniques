'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.is_storage\ntorch.is_storage(obj)\n'
import torch
a = torch.randn(3, 3)
b = torch.randn(3, 3)
print(torch.is_storage(a))
print(torch.is_storage(b))
print(torch.is_storage((a + b)))
print(torch.is_storage((a * b)))