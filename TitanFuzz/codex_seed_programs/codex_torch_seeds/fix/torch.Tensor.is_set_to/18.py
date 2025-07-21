'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_set_to\ntorch.Tensor.is_set_to(_input_tensor, tensor)\n'
import torch
_input_tensor = torch.rand(2, 3)
is_set_to_result = torch.Tensor.is_set_to(_input_tensor, _input_tensor)
print(is_set_to_result)