'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.new_empty\ntorch.Tensor.new_empty(_input_tensor, size, dtype=None, device=None, requires_grad=False)\n'
import torch
_input_tensor = torch.randint(0, 10, (3, 3), dtype=torch.float32)
print('Input Tensor: ', _input_tensor)
_output_tensor = torch.Tensor.new_empty(_input_tensor, (3, 3))
print('Output Tensor: ', _output_tensor)