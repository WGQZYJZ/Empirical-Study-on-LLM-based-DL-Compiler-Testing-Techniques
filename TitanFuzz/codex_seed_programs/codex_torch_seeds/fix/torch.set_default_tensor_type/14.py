'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_default_tensor_type\ntorch.set_default_tensor_type(t)\n'
import torch
x = torch.rand(5, 3)
print(x)
torch.set_default_tensor_type(torch.DoubleTensor)
y = torch.rand(5, 3)
print(y)