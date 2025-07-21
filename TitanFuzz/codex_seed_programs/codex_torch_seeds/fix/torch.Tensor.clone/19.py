'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.clone\ntorch.Tensor.clone(_input_tensor, *, memory_format=torch.preserve_format)\n'
import torch
import torch
_input_tensor = torch.rand(10, 10)
_output_tensor = _input_tensor.clone()
print(_output_tensor)