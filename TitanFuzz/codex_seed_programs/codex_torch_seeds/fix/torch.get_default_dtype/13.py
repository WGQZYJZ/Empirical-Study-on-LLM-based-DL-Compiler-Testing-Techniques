'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.get_default_dtype\ntorch.get_default_dtype()\n'
import torch
x = torch.randn(5, 3)
y = torch.randn(5, 3)
print(torch.get_default_dtype())
'\nTask 4: Call the API torch.set_default_dtype\ntorch.set_default_dtype(torch.float64)\n'
torch.set_default_dtype(torch.float64)
print(torch.get_default_dtype())
'\nTask 5: Call the API torch.set_default_dtype\ntorch.set_default_dtype(torch.float32)\n'
torch.set_default_dtype(torch.float32)
print(torch.get_default_dtype())
'\nTask 6: Call the API torch.set_default_dtype\ntorch.set_default_dtype(torch.float64)\n'
torch.set_default_dtype(torch.float64)
print