'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.all\ntorch.Tensor.all(_input_tensor, dim=None, keepdim=False)\n'
import torch
_input_tensor = torch.Tensor([[True, True, True], [False, False, False]])
print(torch.Tensor.all(_input_tensor, dim=None, keepdim=False))
print(torch.Tensor.all(_input_tensor, dim=0, keepdim=False))
print(torch.Tensor.all(_input_tensor, dim=1, keepdim=False))
print(torch.Tensor.all(_input_tensor, dim=None, keepdim=True))
print(torch.Tensor.all(_input_tensor, dim=0, keepdim=True))
print(torch.Tensor.all(_input_tensor, dim=1, keepdim=True))