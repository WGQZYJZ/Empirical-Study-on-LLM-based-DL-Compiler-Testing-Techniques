'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.trapz\ntorch.trapz(y, *, dx=1, dim=-1)\n'
import torch
import torch
x = torch.linspace(0, 1, 5)
y = torch.tensor([0, 1, 2, 3, 4])
result = torch.trapz(y, x)
print(result)