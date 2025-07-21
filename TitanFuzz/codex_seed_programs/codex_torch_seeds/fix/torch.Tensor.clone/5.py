'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.clone\ntorch.Tensor.clone(_input_tensor, *, memory_format=torch.preserve_format)\n'
import torch
import torch
_input_tensor = torch.randint(0, 10, (4, 4))
_output_tensor = _input_tensor.clone()
print(_input_tensor)
print(_output_tensor)