'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_default_dtype\ntorch.set_default_dtype(d)\n'
import torch
x = torch.randn(2, 3, dtype=torch.float64)
print('Input data:', x)
torch.set_default_dtype(torch.float32)
print('Default dtype:', torch.get_default_dtype())
print('Input data:', x)
torch.set_default_dtype(torch.float64)
print('Default dtype:', torch.get_default_dtype())
print('Input data:', x)