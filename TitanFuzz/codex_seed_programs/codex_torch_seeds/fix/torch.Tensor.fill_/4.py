'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.fill_\ntorch.Tensor.fill_(_input_tensor, value)\n'
import torch
_input_tensor = torch.Tensor(2, 3)
torch.Tensor.fill_(_input_tensor, value=3.14)
print(_input_tensor)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_contiguous\ntorch.Tensor.is_contiguous(_input_tensor)\n'
import torch
_input_tensor = torch.Tensor(2, 3)
print(torch.Tensor.is_contiguous(_input_tensor))
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_same_size\ntorch.Tensor.is_same_size(_input_tensor, _input_tensor)\n'
import torch
_input_tensor = torch.Tensor(2, 3)
print(torch.Tensor.is_same_size(_input_tensor, _input_tensor))