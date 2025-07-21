'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_default_tensor_type\ntorch.set_default_tensor_type(t)\n'
import torch
a = torch.rand(2, 3)
print(a)
torch.set_default_tensor_type(torch.FloatTensor)
b = torch.rand(2, 3)
print(b)
torch.set_default_tensor_type(torch.DoubleTensor)
c = torch.rand(2, 3)
print(c)