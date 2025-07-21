'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.trapz\ntorch.trapz(y, *, dx=1, dim=-1)\n'
import torch
y = torch.tensor([1.0, 2.0, 3.0, 4.0])
result = torch.trapz(y)
print('result: ', result)