'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.get_default_dtype\ntorch.get_default_dtype()\n'
import torch
x = torch.tensor([[1, 2], [3, 4]])
y = torch.tensor([[5, 6], [7, 8]])
torch.get_default_dtype()
torch.set_default_dtype(torch.float32)
torch.get_default_dtype()
(x.dtype, y.dtype)
torch.set_default_dtype(torch.float64)
torch.get_default_dtype()