'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_default_tensor_type\ntorch.set_default_tensor_type(t)\n'
import torch
a = torch.randn(4, 4)
b = torch.randn(4, 4)
torch.set_default_tensor_type(torch.DoubleTensor)
print(a.dtype)
print(b.dtype)