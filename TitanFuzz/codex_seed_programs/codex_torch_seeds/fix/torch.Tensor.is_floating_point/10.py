'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_floating_point\ntorch.Tensor.is_floating_point(_input_tensor)\n'
import torch
_input_tensor = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype=torch.float32)
_is_floating_point = torch.Tensor.is_floating_point(_input_tensor)
print('Is floating point: ', _is_floating_point)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_signed\ntorch.Tensor.is_signed(_input_tensor)\n'
import torch