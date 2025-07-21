'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_default_dtype\ntorch.set_default_dtype(d)\n'
import torch
input_data = torch.rand(3, 3)
torch.set_default_dtype(torch.float64)
print(input_data.dtype)