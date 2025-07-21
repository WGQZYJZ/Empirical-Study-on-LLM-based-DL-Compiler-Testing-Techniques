'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_floating_point\ntorch.Tensor.is_floating_point(_input_tensor)\n'
import torch
input_tensor = torch.rand(2, 3)
print(input_tensor.is_floating_point())
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_complex\ntorch.Tensor.is_complex(_input_tensor)\n'
import torch
input_tensor = torch.rand(2, 3)
print(input_tensor.is_complex())
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_same_size\ntorch.Tensor.is_same_size(_input_tensor, _other_tensor)\n'
import torch
input_tensor = torch.rand(2, 3)
other_tensor = torch.rand(2, 3)