'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_default_dtype\ntorch.set_default_dtype(d)\n'
import torch
a = torch.tensor([1, 2, 3])
b = torch.tensor([1, 2, 3], dtype=torch.float32)
torch.set_default_dtype(torch.float32)
print(torch.get_default_dtype())
print(a.dtype)
print(b.dtype)