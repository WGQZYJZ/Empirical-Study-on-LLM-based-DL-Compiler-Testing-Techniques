'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.char\ntorch.Tensor.char(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
import numpy as np
_input_tensor = torch.randint(0, 256, (1, 2, 3, 4), dtype=torch.uint8)
_output_tensor = _input_tensor.char()
print(_input_tensor)
print(_output_tensor)