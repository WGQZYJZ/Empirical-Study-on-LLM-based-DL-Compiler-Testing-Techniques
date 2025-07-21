'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_floating_point\ntorch.Tensor.is_floating_point(_input_tensor)\n'
import torch
_input_tensor = torch.randn(1, 2, 3, dtype=torch.float32)
print(_input_tensor.is_floating_point())
print(_input_tensor.is_floating_point(memory_format=torch.channels_last))