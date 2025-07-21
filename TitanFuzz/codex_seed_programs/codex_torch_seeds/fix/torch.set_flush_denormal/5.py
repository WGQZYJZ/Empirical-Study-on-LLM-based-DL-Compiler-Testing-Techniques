'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_flush_denormal\ntorch.set_flush_denormal(mode)\n'
import torch
x = torch.tensor([1e-323], dtype=torch.float32)
print('x = ', x)
torch.set_flush_denormal(True)
print('x = ', x)