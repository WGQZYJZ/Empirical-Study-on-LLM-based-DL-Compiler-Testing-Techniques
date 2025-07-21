'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_default_dtype\ntorch.set_default_dtype(d)\n'
import torch
x = torch.randn(2, 3, dtype=torch.float64)
print(x.dtype)
torch.set_default_dtype(torch.float64)
y = torch.randn(2, 3)
print(y.dtype)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_default_tensor_type\ntorch.set_default_tensor_type(t)\n'
import torch
x = torch.randn(2, 3, dtype=torch.float64)
print(x.dtype)
torch.set_default_tensor_type(torch.FloatTensor)
y = torch.randn(2, 3)
print(y.dtype)