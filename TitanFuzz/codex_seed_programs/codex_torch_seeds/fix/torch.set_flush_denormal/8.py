'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_flush_denormal\ntorch.set_flush_denormal(mode)\n'
import torch
import torch
x = torch.tensor([1e-323], dtype=torch.float32)
torch.set_flush_denormal(True)
print('x:', x)
print('x.dtype:', x.dtype)
print('x.item():', x.item())
torch.set_flush_denormal(False)
print('x:', x)
print('x.dtype:', x.dtype)
print('x.item():', x.item())