'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.argmax\ntorch.Tensor.argmax(_input_tensor, dim=None, keepdim=False)\n'
import torch
_input_tensor = torch.rand(2, 3)
print(_input_tensor)
print(torch.Tensor.argmax(_input_tensor, dim=None, keepdim=False))
print(torch.Tensor.argmax(_input_tensor, dim=0, keepdim=False))
print(torch.Tensor.argmax(_input_tensor, dim=1, keepdim=False))
print(torch.Tensor.argmax(_input_tensor, dim=None, keepdim=True))
print(torch.Tensor.argmax(_input_tensor, dim=0, keepdim=True))
print(torch.Tensor.argmax(_input_tensor, dim=1, keepdim=True))