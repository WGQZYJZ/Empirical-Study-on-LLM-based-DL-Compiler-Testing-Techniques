'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.all\ntorch.Tensor.all(_input_tensor, dim=None, keepdim=False)\n'
import torch
input_tensor = torch.randn(3, 3)
print('Input Tensor:\n', input_tensor)
all_tensor = torch.Tensor.all(input_tensor)
print('All Tensor:\n', all_tensor)
all_tensor = torch.Tensor.all(input_tensor, dim=0)
print('All Tensor:\n', all_tensor)
all_tensor = torch.Tensor.all(input_tensor, dim=1)
print('All Tensor:\n', all_tensor)
all_tensor = torch.Tensor.all(input_tensor, dim=1, keepdim=True)
print('All Tensor:\n', all_tensor)