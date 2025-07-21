'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cummin\ntorch.Tensor.cummin(_input_tensor, dim)\n'
import torch
_input_tensor = torch.randint(low=0, high=10, size=(3, 4), dtype=torch.float32)
print('Input Tensor:\n', _input_tensor)
_output_tensor = torch.Tensor.cummin(_input_tensor, dim=0)
print('Output Tensor:\n', _output_tensor)