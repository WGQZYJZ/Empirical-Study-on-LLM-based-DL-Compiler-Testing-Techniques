'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.half\ntorch.Tensor.half(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
_input_tensor = torch.randn((3, 3), dtype=torch.float32)
_half_tensor = _input_tensor.half()
print(_half_tensor)