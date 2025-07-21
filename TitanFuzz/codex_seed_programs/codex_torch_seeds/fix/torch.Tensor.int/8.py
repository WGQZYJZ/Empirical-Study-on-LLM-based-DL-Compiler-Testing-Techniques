'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.int\ntorch.Tensor.int(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
_input_tensor = torch.randint(low=0, high=10, size=(5, 5), dtype=torch.int32)
print('Input tensor: {}'.format(_input_tensor))
_output_tensor = _input_tensor.int()
print('Output tensor: {}'.format(_output_tensor))