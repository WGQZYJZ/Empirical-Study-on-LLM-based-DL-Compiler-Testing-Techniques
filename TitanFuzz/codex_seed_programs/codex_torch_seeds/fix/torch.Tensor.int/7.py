'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.int\ntorch.Tensor.int(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
_input = torch.randn(2, 3, 4, 5)
_input_tensor = torch.Tensor.int(_input)
print('Tensor.int(_input): ', _input_tensor)