'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_default_dtype\ntorch.set_default_dtype(d)\n'
import torch
x = torch.tensor(2.0, dtype=torch.float32)
torch.set_default_dtype(torch.float64)
print(x.dtype)
print(torch.get_default_dtype())