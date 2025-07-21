'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.randn_like\ntorch.randn_like(input, *, dtype=None, layout=None, device=None, requires_grad=False, memory_format=torch.preserve_format)\n'
import torch
import torch
data = torch.randn(2, 3)
torch.randn_like(data)
print(torch.randn_like(data))
print(torch.randn_like(data).shape)
print(torch.randn_like(data).dtype)
print(torch.randn_like(data).device)
print(torch.randn_like(data).requires_grad)