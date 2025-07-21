'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.get_default_dtype\ntorch.get_default_dtype()\n'
import torch
input_data = torch.randn(5, 3)
print(torch.get_default_dtype())
torch.set_default_dtype(torch.double)
print(torch.get_default_dtype())
torch.set_default_dtype(torch.float32)
print(torch.get_default_dtype())